# -*- coding: utf-8 -*-
import scrapy
from ..items import FontprojectItem

class FontsSpider(scrapy.Spider):
    name = 'fonts'
    start_urls = [
        'https://www.dafont.com/mtheme.php?id=1'
        'https://www.dafont.com/mtheme.php?id=2&fpp=200',
        'https://www.dafont.com/mtheme.php?id=3&fpp=200',
        'https://www.dafont.com/mtheme.php?id=4&fpp=200',
        'https://www.dafont.com/mtheme.php?id=5&fpp=200',
        'https://www.dafont.com/mtheme.php?id=6&fpp=200',
        'https://www.dafont.com/mtheme.php?id=7&fpp=200',
        'https://www.dafont.com/mtheme.php?id=8&fpp=200',
    ]

    def parse(self, response):

        font_links = response.css('.preview a::attr(href)').getall()
        for page in font_links:
            url = response.urljoin(page)
            yield scrapy.Request(url, callback=self.parse_font_page)

        page_links = response.css('.noindex a')
        next_page = None
        for x in page_links:
            if x.css('::attr(title)').get() == "Keyboard shortcut: Right arrow":
                next_page = response.urljoin(x.css('::attr(href)').get())
                break

        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)


    def parse_font_page(self,response):

        item = FontprojectItem()

        name = response.css('.lv1left strong::text').get()
        author = response.css('.lv1left a::text').get()

        category = response.css('.lv1right a::text').getall()
        main = category[0]
        sub = category[1]

        down = response.css('.dlbox a::attr(href)').get()
        img = response.css('.preview::attr(style)').get().split('(')[1][:-1]

        item['font_name'] = name
        item['font_author'] = author
        item['font_main_category'] = main
        item['font_sub_category'] = sub
        item['font_download'] = down
        item['font_image'] = response.urljoin(img)

        yield item






