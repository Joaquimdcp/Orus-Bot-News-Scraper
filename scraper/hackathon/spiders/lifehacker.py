# -*- coding: utf-8 -*-
import scrapy
import prova1


class QuotesSpider(scrapy.Spider):
    name = 'lifehacker'
    base = 'http://www.lifehacker.net'
    portada = True
    k = 0
    links_next = []
    def start_requests(self):
        url = 'http://www.lifehacker.net'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if(self.portada):
            self.links_next.append(response.xpath('//*[@class="headline entry-title js_entry-title featured"]/a/@href').extract_first())
            self.links_next = self.links_next + response.xpath('//*[@class="headline entry-title js_entry-title"]/a/@href').extract()
            self.portada = False
            yield scrapy.Request(url=self.links_next[0], callback=self.parse)
        else:
            self.k+=1
            llista_textos = []
            if(self.k<len(self.links_next)):
                llista_textos.append(response.xpath('//*[@class="headline hover-highlight entry-title js_entry-title"]/a/text()').extract_first())
                llista_textos = response.xpath('//p/text()').extract()
                sol = prova1.get_tags_and_sentiment(llista_textos)
                yield scrapy.Request(url=self.links_next[self.k], callback=self.parse)
