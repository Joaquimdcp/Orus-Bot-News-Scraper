# -*- coding: utf-8 -*-
import scrapy
import resum

from elasticsearch import Elasticsearch


import json

class QuotesSpider(scrapy.Spider):
    name = 'theforce'
    base = 'http://www.theforce.net'
    portada = True
    k = 0
    links_next = []
    textos = []
    def start_requests(self):
        self.url = 'http://www.theforce.net/'
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        print("HOLAAA")
        if(self.portada):
            print "provaa"
            l_next = response.xpath('//*[@class="title"]/@href').extract()
            for l in l_next:
                print self.base + l
                self.links_next.append(self.base + l)
            self.portada = False
            yield scrapy.Request(url=self.links_next[0], callback=self.parse)
        else:
            self.k+=1
            llista_textos = []
            if(self.k<len(self.links_next)):
                prova = response.xpath('//*[@class="news-headline"]/text()').extract_first()
                llista_textos = response.xpath('//*[@class="news-teaser-content"]/text()').extract()
                n = ' '.join(llista_textos)



                texts = [prova, n]
                self.textos.append(texts)

                yield scrapy.Request(url=self.links_next[self.k], callback=self.parse)
            else:
                sets = resum.get_database(self.textos)

                es = Elasticsearch(
                    ['ec2-54-191-86-108.us-west-2.compute.amazonaws.com'],
                    port=9200
                )
                prova = True
                for s in sets:
                    if(prova):
                        d = {'cos': s[1],
                             'index': s[0]}
                        s = json.dumps(d, encoding='ISO-8859-1')
                        res = es.index(index='articles', doc_type='feeds', body= s)
