# -*- coding: utf-8 -*-
import scrapy
import prova1


class QuotesSpider(scrapy.Spider):
    name = 'prova'
    portada = True
    k = 0
    links_next = []
    def start_requests(self):
        urls = 'http://www.lavanguardia.com/'
        yield scrapy.Request(url=urls, callback=self.parse)

    def parse(self, response):
        if(self.portada):
            print "HOLA"
            #self.links_next.append(response.xpath('//*[@class="mod-title normal"]/a/@href').extract_first())
            #self.links_next = self.links_next + response.xpath('//*[@class="flex-article__heading"]/a/@href').extract()
            #self.links_next = self.links_next + response.xpath('//*[@class="mod-title normal"]/a/@href').extract()
            #self.portada = False
            #yield scrapy.Request(url=self.links_next[0], callback=self.parse)
        else:
            self.k+=1
            llista_textos = []
            if(self.k<len(self.links_next)):
                llista_textos.append(response.xpath('//*[@itemprop="headline"]/text()').extract_first())
                llista_textos = response.xpath('//p/text()').extract()
                sol = prova1.get_tags_and_sentiment(llista_textos)
                print sol
                yield scrapy.Request(url=self.links_next[self.k], callback=self.parse)
