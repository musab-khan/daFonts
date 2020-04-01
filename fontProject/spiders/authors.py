# -*- coding: utf-8 -*-
import scrapy
from ..items import authorsItem
class AuthorsSpider(scrapy.Spider):
    name = 'authors'
    start_urls = ['https://www.dafont.com/authors.php']

    def parse(self, response):

        country_links = response.css('.dfsmall a::attr(href)').getall()

        for link in country_links:
            url = response.urljoin(link)
            yield scrapy.Request(url, callback=self.parseAuthor)

    def parseAuthor(self,response):
        record = authorsItem()

        authors = response.css('.tdn div div div a')
        country = response.css('.dfsmall b::text').getall()[2].split('(')[0]

        for x in authors:
            name = x.css('::text').get()
            link = response.urljoin(x.css('::attr(href)').get())

            record['author_country'] = country
            record['author_name'] = name
            record['author_link'] = link

            yield record
