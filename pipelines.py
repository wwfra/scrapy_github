# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy_github.items.user_item import UserItem
from scrapy_github.items.repo_item import RepoItem
from scrapy_github.items.org_item import OrgItem
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class UserPipeline:
    """
    用户管道
    """
    def __init__(self):
        self.file = None

    def open_spider(self, spider):
        self.file = open('user.json', 'a', encoding='utf-8')

    def close_spider(self, spider):
        if self.file:
            self.file.close()

    def process_item(self, item, spider):
        if isinstance(item, UserItem):
            data = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file.write(data)
            return None
        else:
            return item


class RepoPipeline:
    """
    仓库管道
    """
    def __init__(self):
        self.file = None

    def open_spider(self, spider):
        self.file = open('repo.json', 'a', encoding='utf-8')

    def close_spider(self, spider):
        if self.file:
            self.file.close()

    def process_item(self, item, spider):
        if isinstance(item, RepoItem):
            data = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file.write(data)
            return None
        else:
            return item


class OrgPipeline:
    """
    组织管道
    """
    def __init__(self):
        self.file = None

    def open_spider(self, spider):
        self.file = open('org.json', 'a', encoding='utf-8')

    def close_spider(self, spider):
        if self.file:
            self.file.close()

    def process_item(self, item, spider):
        if isinstance(item, OrgItem):
            data = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file.write(data)
            return None
        else:
            return item
