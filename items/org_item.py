# -*- coding: utf-8 -*-
"""
作者: Liwz
日期: 2023/06/18
"""
import scrapy


class OrgItem(scrapy.Item):
    # Organization
    """
    参数说明:
    org_1_name:     组织名
    org_2_page:     组织主页URL
    org_3_repo:     组织仓库数
    org_4_follower: 组织粉丝数
    """
    org_1_name = scrapy.Field()
    org_2_page = scrapy.Field()
    org_3_repo = scrapy.Field()
    org_4_follower = scrapy.Field()
