from primeWireSpider.items import PrimewirespiderItem

from scrapy.spiders import CrawlSpider

class PrimeWire(CrawlSpider):
	name = 'Prime'
	start_urls= []
	def __init__(self):
		for s in  range(2,100):
			tmp=str(s)
			self.start_urls.append("http://www.primewire.ag/index.php?page=%d"%(s))



	def parse(self,response):
		items = []
		select = response.css("div.container div.main_body div.col1 div.index_container div.index_item")
		for s in select:
			prime = PrimewirespiderItem()
			prime['name']=s.css("h2::text").extract()
			prime['url']=s.css("a::attr(href)").extract()
			items.append(prime)

		yield items