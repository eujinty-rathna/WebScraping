import scrapy
import re
from ..items import RedtapeItem
class RedtapeshoesSpider(scrapy.Spider):
    name = "redtapeshoes"
    cookies = {
        '_gcl_au': '1.1.1505067918.1678684019',
        '_fbp': 'fb.1.1678684019917.1565117906',
        'OCSESSID': '0f7e1f0ad0e9e195eb74f81805',
        'language': 'en-gb',
        'currency': 'INR',
        '_gid': 'GA1.2.1700747633.1682488282',
        '_ga_0K9PYNHBKR': 'GS1.1.1682488282.4.1.1682488302.0.0.0',
        '_ga': 'GA1.2.1501416539.1678684019',
        '_gat_UA-39850473-1': '1',
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,ta;q=0.8,hi;q=0.7',
        'Connection': 'keep-alive',
        # 'Cookie': '_gcl_au=1.1.1505067918.1678684019; _fbp=fb.1.1678684019917.1565117906; OCSESSID=0f7e1f0ad0e9e195eb74f81805; language=en-gb; currency=INR; _gid=GA1.2.1700747633.1682488282; _ga_0K9PYNHBKR=GS1.1.1682488282.4.1.1682488302.0.0.0; _ga=GA1.2.1501416539.1678684019; _gat_UA-39850473-1=1',
        'DNT': '1',
        'Referer': 'https://redtape.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    def start_requests(self):
        url = 'https://www.redtape.com/'
        yield scrapy.Request(url,headers=self.headers,cookies=self.cookies,callback=self.get_category_urls)

    def get_category_urls(self, response):
        all_urls = response.xpath('//a/@href').getall()
        category_urls = [link for link in all_urls if re.search(
            r".*w?o?men-footwear$|.*/kids.*/.*flip-flops$|.*/kids.*/.*sports-shoes$", link)]
        for url in category_urls:
            print(url)
            yield  response.follow(url, headers=self.headers,cookies=self.cookies,callback=self.get_product_urls)
    def get_product_urls(self,response):
        all_products = response.css('a.recordclickevent::attr(href)').getall()
        for url in all_products:
            yield  response.follow(url,headers=self.headers,cookies=self.cookies,callback=self.parse)
        next_page = response.css('a:contains(">")')
        if next_page:
            next_page = response.css('a:contains(">")::attr(href)').get()
            print(next_page)
            yield response.follow(next_page,headers=self.headers,cookies=self.cookies,callback=self.get_product_urls)
    def parse(self,response):
        def parse_with_xpath(query):
            return response.xpath(query).get(default='').strip()
        name = parse_with_xpath('//h1[@class="main-heading mb-5 txt-c"]/text()')
        price = response.xpath('//h2/text()').re_first(r'.*\d+')
        sizes = response.xpath('//div[@class="radio span-option-div "]/label/span/text()').getall()
        mrp = parse_with_xpath('//span[@style="text-decoration: line-through;"]/text()')
        color_brand_model = response.xpath('//ul[@class="list-unstyled col-flex pcode"]/li').re(r'</b>(.*)</li>')
        try:
            color = color_brand_model[0]
            brand = color_brand_model[1]
            model = color_brand_model[2]
        except:
            color ,brand,model = '','',''
        item = RedtapeItem()
        item['name'] = name
        item['mrp'] = mrp
        item['price'] = price
        item['sizes'] = sizes
        item['colour'] = color
        item['model'] = model
        item['brand']  = brand
        yield  item