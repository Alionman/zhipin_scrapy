# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import ZhipinItem
import pickle
from scrapy.linkextractors import LinkExtractor

class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    main_url = 'https://www.zhipin.com/?ka=header-home'

    def start_requests(self):
        cookies = pickle.load(open("cookies.pkl","rb"))
        yield Request(self.main_url, cookies = cookies, callback = self.parse)

    def parse(self, response):
        le = LinkExtractor(restrict_css="div.job-menu > dl:first-child div.menu-sub")
        links = le.extract_links(response)
        for link in links:
            yield Request(link.url, callback = self.parse_info)      

    def parse_info(self, response):
        info = ZhipinItem()
        info['job_type'] = response.css("div.position-sel span.label-text b::text").extract_first()
        sal_str = response.css("div.job-list li span.red::text").extract()
        info['salary'] = ','.join(sal_str)
        company_list = response.css('div.job-list li div.info-company a::text').extract()
        info['company'] = ','.join(company_list)
        
        yield info


        

        
