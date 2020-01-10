# -*- coding: utf-8 -*-
from scrapy.exporters import JsonItemExporter #Json数据的模块导入

class MyScrapyPipeline(object):

    def open_spider(self,spider):
        self.file=open('sxew.json','wb')
        self.writer=JsonItemExporter(self.file)
        self.writer.start_exporting()

    def close_spider(self,spider):
        self.writer.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):

        print("==========启动管道")
        self.writer.export_item(item)
        return item

#
# class MyScrapyPipeline(object):
#     def process_item(self, item, spider):
#         print(item)
#         return