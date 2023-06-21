# -*- coding: utf-8 -*-
"""
作者: Liwz
日期: 2023/06/16
"""
import scrapy


class UserItem(scrapy.Item):
    # User
    """
    参数说明:
    user_1_name:        用户名
    user_2_page:        用户主页URL
    user_3_star:        用户收藏数
    user_4_repo:        用户仓库数
    user_5_follower:    用户粉丝数
    user_6_following:   用户关注数
    """
    user_1_name = scrapy.Field()
    user_2_page = scrapy.Field()
    user_3_star = scrapy.Field()
    user_4_repo = scrapy.Field()
    user_5_follower = scrapy.Field()
    user_6_following = scrapy.Field()
