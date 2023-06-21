# -*- coding: utf-8 -*-
"""
作者: Liwz
日期: 2023/06/16
"""

import scrapy


class RepoItem(scrapy.Item):
    # Repositories
    """
    参数说明:
    repo_1_name:    仓库名
    repo_2_star:    仓库收藏数
    repo_3_watch:   仓库浏览量
    repo_4_fork:    仓库分支数
    """
    repo_1_name = scrapy.Field()
    repo_2_star = scrapy.Field()
    repo_3_watch = scrapy.Field()
    repo_4_fork = scrapy.Field()
