# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZhipinPipeline(object):
    def process_item(self, item, spider):
        sal_string = item.get('salary')
        if sal_string:
            sal_str = sal_string.split(',')
            sal_sum = 0
            sal_int = []
            for salary in sal_str:
                sal_int.append(salary.split('-')[0].strip('k'))
                sal_int.append(salary.split('-')[1].strip('k'))
            for salary in sal_int:
                sal_sum += int(salary)
            item['salary'] = '%.2f' % (sal_sum/len(sal_int)) 
        return item
