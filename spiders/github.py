import scrapy
from time import sleep
from scrapy_github.items import user_item, repo_item, org_item


class GithubSpider(scrapy.Spider):
    name = "github"

    # allowed_domains = ["github.com"]
    # start_urls = ["https://github.com/search?q=followers:>10000&type=users&s=followers&o=desc"]

    def set_url(self, q=None, expr=None, language=None, s=None, start=None, stop=None):
        """
        设置初始URL:
        参数说明:
            param:q:    str     查询内容["stars", "forks", "followers", "repos", "location"]
            param:expr: str     查询条件[":>10000" --> 数值大于10000]
            param:type: str     查询类型["Users", "Repositories"]
            param:l:    str     查询语言["java", "python", "C"...]
            param:s:    str     排序依据["stars", "followers", "repositories"]
            param:start:int     起始页面
            param:stop: int     结束页面
        """
        q_type = " "
        sign = 0  # 判断爬取类型以选择正确的爬取方法
        if q in ["stars", "forks"]:
            q_type = "Repositories"
        elif q in ["followers", "repos", "location"]:
            q_type = "Users"
            sign = 1
        urls = ['https://github.com/search?q={q}:{expr}&type={type}&l={l}&s={s}&o=desc&p={p}'.
                format(q=q, expr=expr, type=q_type, l=language, s=s, p=p) for p in range(start, stop)]
        return urls, sign

    def start_requests(self):
        """
        爬虫入口
        方法分支：
            self.parse_user:    查询用户类数据
            self.parse_repos:   查询仓库类数据
        """
        urls, sign = self.set_url(q="followers", expr=">10000", language="all", s="followers", start=1, stop=2)
        sleep(5)
        if sign == 1:
            for url in urls:
                print('===============Request User===============')
                yield scrapy.Request(url=url, callback=self.parse_user)
        else:
            for url in urls:
                print('===============Request Repo===============')
                yield scrapy.Request(url=url, callback=self.parse_repos)

    def parse_user(self, response):
        """
        初步解析用户列表
        提取待爬取用户
        并回调给下一级解析方法
        """
        user_names = response.xpath('//div[@data-testid="results-list"]//h3//a[1]/span//text()').extract()
        user_pages = response.xpath('//div[@data-testid="results-list"]//h3//a[1]/@href').extract()
        print('user_names=', user_names)
        print('user_pages=', user_pages)
        for name, page in zip(user_names, user_pages):
            url = "https://github.com{}".format(page)
            print('++++++++++wait 10s++++++++++')
            sleep(20)
            print('parse_user_page:', url)
            yield scrapy.Request(url=url, callback=self.parse_user_page, meta={'name': name, 'url': url})

    def parse_user_page(self, response):
        """
        深度解析每位用户/组织主页
        返回包括上一步爬到的用户信息一并提交管道
        """
        isOrg = response.xpath('//div[@class="AppHeader-localBar"]/nav/@aria-label').extract()
        # 判断是否为组织
        if not isOrg:
            isOrg = ['Organization']
        # Organization
        if isOrg[0] == 'Organization':
            org_name = response.meta['name']
            org_page = response.meta['url']
            org_repo = response.xpath('//*[@id="repositories-tab"]/span[2]/text()').extract()
            org_follower = response.xpath(
                '/html/body/div[1]/div[6]/main/div/header/div/div/div[2]/div[2]/ul/li[1]/a/span/text()').extract()
            if not org_repo:
                org_repo = ['0']
            if not org_follower:
                org_follower = ['0']
            print('org_name=', org_name)
            print('org_page=', org_page)
            print('org_repo=', org_repo[0])
            print('org_follower=', org_follower[0])

            org = org_item.OrgItem()
            org['org_1_name'] = org_name
            org['org_2_page'] = org_page
            org['org_3_repo'] = org_repo[0]
            org['org_4_follower'] = org_follower[0]
            yield org
        # User
        else:
            user_name = response.meta['name']
            user_page = response.meta['url']
            user_star = response.xpath('//a[@id="stars-tab"]/span[2]/text()').extract()
            user_repo = response.xpath('//a[@id="repositories-tab"]/span[2]/text()').extract()
            user_follower = response.xpath('//div[@class="mb-3"]/a[1]/span/text()').extract()
            user_following = response.xpath('//div[@class="mb-3"]/a[2]/span/text()').extract()
            if not user_star:
                user_star = ['0']
            if not user_repo:
                user_repo = ['0']
            if not user_follower:
                user_follower = ['0']
            if not user_following:
                user_following = ['0']
            print('user_name=', user_name)
            print('user_page=', user_page)
            print('user_star=', user_star[0])
            print('user_repo=', user_repo[0])
            print('user_follower=', user_follower[0])
            print('user_following=', user_following[0])

            user = user_item.UserItem()
            user['user_1_name'] = user_name
            user['user_2_page'] = user_page
            user['user_3_star'] = user_star[0]
            user['user_4_repo'] = user_repo[0]
            user['user_5_follower'] = user_follower[0]
            user['user_6_following'] = user_following[0]
            yield user

    def parse_repos(self, response):
        """
        初步解析仓库列表
        提取待爬取仓库
        并回调给下一级解析方法
        """
        repo_names = response.xpath('//div[@data-testid="results-list"]//h3//a[1]/span/text()').extract()
        print('repo_names=', repo_names)
        for name in repo_names:
            url = "https://github.com/{}".format(name)
            print('++++++++++wait 10s++++++++++')
            sleep(10)
            print('parse_repos_page:', url)
            yield scrapy.Request(url=url, callback=self.parse_repos_page, meta={'name': name})

    def parse_repos_page(self, response):
        """
        深度解析每个仓库主页
        返回包括上一步爬到的仓库信息一并提交管道
        """
        # top_language = '//div/a/span/span[@itemprop="programmingLanguage"]'
        repo_name = response.meta['name']
        repo_star = response.xpath('//span[@id="repo-stars-counter-star"]/text()').extract()
        repo_watch = response.xpath('//span[@id="repo-notifications-counter"]/text()').extract()
        repo_fork = response.xpath('//span[@id="repo-network-counter"]/text()').extract()
        if not repo_star:
            repo_star = ['0']
        if not repo_watch:
            repo_watch = ['0']
        if not repo_fork:
            repo_fork = ['0']
        print('repo_name=', repo_name)
        print('repo_star=', repo_star[0])
        print('repo_watch=', repo_watch[0])
        print('repo_fork=', repo_fork[0])

        repo = repo_item.RepoItem()
        repo['repo_1_name'] = repo_name
        repo['repo_2_star'] = repo_star[0]
        repo['repo_3_watch'] = repo_watch[0]
        repo['repo_4_fork'] = repo_fork[0]
        yield repo
