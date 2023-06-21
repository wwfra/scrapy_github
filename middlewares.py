# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from time import sleep
from scrapy.http import HtmlResponse
from scrapy_github.utils import create_chrome_driver

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class ScrapyGithubDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def __init__(self):
        """
        初始化浏览器
        模拟登陆
        """
        self.browser = create_chrome_driver()
        self.browser.get('https://github.com/login')
        sleep(5)
        input_name = self.browser.find_element(by='xpath', value='//*[@id="login_field"]')
        input_name.send_keys('用户名')
        input_pwd = self.browser.find_element(by='xpath', value='//*[@id="password"]')
        input_pwd.send_keys('密码')
        sleep(3)
        sign_in = self.browser.find_element(by='xpath', value='//*[@id="login"]/div[4]/form/div/input[13]')
        sign_in.click()

    def __del__(self):
        """
        爬虫结束关闭资源
        """
        self.browser.close()

    def process_request(self, request, spider):
        """
        处理动态页面
        """
        print('++++++++++process_request++++++++++')
        self.browser.get(request.url)
        sleep(5)
        page_source = self.browser.page_source
        response = HtmlResponse(url=request.url, body=page_source, encoding='utf-8', request=request)
        return response
