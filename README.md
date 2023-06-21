[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
# scrapy_github
本程序可以针对GitHub上最热门的用户与仓库进行爬取和解析，[数据类型](https://github.com/wwfra/scrapy_github#%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B)包括用户、组织和仓库三大类，运行前请参考[注意事项](https://github.com/wwfra/scrapy_github#%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9)
## 程序整体框架图

## 数据类型
### 用户类数据
- user_1_name:        用户名
- user_2_page:        用户主页URL
- user_3_star:        用户收藏数
- user_4_repo:        用户仓库数
- user_5_follower:    用户粉丝数
- user_6_following:   用户关注数
### 组织类数据
- org_1_name:     组织名
- org_2_page:     组织主页URL
- org_3_repo:     组织仓库数
- org_4_follower: 组织粉丝数
### 仓库类数据
- repo_1_name:    仓库名
- repo_2_star:    仓库收藏数
- repo_3_watch:   仓库浏览量
- repo_4_fork:    仓库分支数
## 开发环境
- 开发语言：python3
- 操作系统： Windows/Linux/macOS
## 注意事项
- 运行前需修改middlewares.py中的对应用户名密码
- 运行前需修改utils.py中的对应浏览器驱动地址
