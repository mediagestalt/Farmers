import scrapy
from farmfresh.items import FarmfreshItem

class FarmfreshSpider(scrapy.Spider):
	name = "farmfresh"
	download_delay = 5
	allowed_domains = ["guide.albertafarmfresh.com/"]
	start_urls = ["http://guide.albertafarmfresh.com/page/location/pageid/223085/", "http://guide.albertafarmfresh.com/page/location/pageid/223065/", "http://guide.albertafarmfresh.com/page/location/pageid/223084/", "http://guide.albertafarmfresh.com/page/location/pageid/223082/", "http://guide.albertafarmfresh.com/page/location/pageid/216364/" ]

	def parse(self, response):
		sel = scrapy.Selector(response)
		requests = sel.xpath('//script[@type="text/javascript"]')
		itemlist = []
		for r in requests:
			item = FarmfreshItem()
			item['name'] = r.xpath('//div[@class="full"]/ul/li/a/h1/text()').extract()
			item['gis'] = r.xpath('//script').re(r'LatLng(\([0-9.]+,-[0-9.]+\))')
			item['name1'] = r.xpath('//script').re(r'infowindow\.setContent\(\'<div style=\"color: #000 !important;\"><b>(\w+\W+.?)')
			itemlist.append(item)
			return itemlist
