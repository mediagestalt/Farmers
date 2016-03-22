import scrapy
from farmers.items import FarmersItem

class FarmersSpider(scrapy.Spider):
	name = "farmers"
	download_delay = 5
	allowed_domains = ["www.albertamarkets.com"]
	start_urls = ["http://www.albertamarkets.com/vendors/search-vendors"]

	def parse(self, response):
		sel = scrapy.Selector(response)
		requests = sel.xpath('//*[@class="searchResults"]/div[@class="marketContainer"]')
		itemlist = []
		for r in requests:
			item = FarmersItem()
			item['name'] = r.xpath('./h2/text()').extract()
			item['category'] = r.xpath('./table/tr/td/table[@class="categoryInfoTable"]/tr/td/text()').extract()
			item['email'] = r.xpath('./table/tr/td/div[@class="email"]/text()').extract()
			item['phone'] = r.xpath('./table/tr/td/div[@class="phone"]/text()').extract()
			item['location'] = r.xpath('./table/tr/td/div[@class="location"]/text()').extract()
			item['markets'] = r.xpath('./table/tr/td[@class="vendorMarkets"]/ul/li//a/text()').extract()
			item['website'] = r.xpath('./table/tr/td/div[@class="website"]/a/text()').extract()
			itemlist.append(item)
		return itemlist
