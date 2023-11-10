# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class CSVExportPipeline:
    def __init__(self):
        self.csv_file = open('urls.csv', 'w', newline='')
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow(['URL'])  # Write header row

    def process_item(self, item, spider):
        self.csv_writer.writerow(item['url'])
        return item

    def close_spider(self, spider):
        self.csv_file.close()

class EnginePipeline:
    def process_item(self, item, spider):
        return item
