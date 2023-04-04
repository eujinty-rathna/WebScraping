import re
from aldoshoes.items import AldoshoesItem
import scrapy
from scrapy.selector import Selector
from price_parser import  Price

class AldoSpider(scrapy.Spider):
    name = "aldo"
    start_urls = ["https://www.aldoshoes.in/robots.txt"]
    cookies = {
        'dwanonymous_5b1426a9b1add3e91ed7230c2c4c5c66': 'cfxgKdthCHOaebA45Ibr0LqSEc',
        '__cq_uuid': 'cdESI4NmcINb76d5RZlFoxpaYh',
        '_gac_UA-147961841-1': '1.1679374475.EAIaIQobChMItfe7tJ3s_QIVRn8rCh0GnwDNEAAYASAAEgJK4vD_BwE',
        '_gcl_aw': 'GCL.1679374475.EAIaIQobChMItfe7tJ3s_QIVRn8rCh0GnwDNEAAYASAAEgJK4vD_BwE',
        '_gcl_au': '1.1.1525965429.1679374475',
        '_fbp': 'fb.1.1679374475455.1541884172',
        '_gid': 'GA1.2.1636619829.1680011119',
        'dwac_099d1b7f0f12b2ec36af62feb3': '-D51gYEcxyc1FdOCVMS0aAq97V79I-ejm-I%3D|dw-only|||INR|false|Asia%2FKolkata|true',
        'cqcid': 'cfxgKdthCHOaebA45Ibr0LqSEc',
        'cquid': '||',
        'sid': '-D51gYEcxyc1FdOCVMS0aAq97V79I-ejm-I',
        '__cq_dnt': '0',
        'dw_dnt': '0',
        'dwsid': 'xBfqFtHq0SKCwYXMZIp66zaUcsmt1fGmLDYuyEClnuHptOgy6E9k2gj5MQO1LKY5UuE0Riccopq1tf01UrfPTw==',
        '_ga_5FDJMYHPK9': 'GS1.1.1680063880.5.1.1680065161.0.0.0',
        '__cq_bc': '%7B%22bgsc-aldo-shoes%22%3A%5B%7B%22id%22%3A%22ZULIAN001%22%7D%2C%7B%22id%22%3A%22REX115043%22%7D%2C%7B%22id%22%3A%22REX001043%22%7D%2C%7B%22id%22%3A%22GENTO001043%22%7D%2C%7B%22id%22%3A%22AERUS271041%22%7D%2C%7B%22id%22%3A%22ACES100043%22%7D%5D%7D',
        '__cq_seg': '0~-0.04!1~0.39!2~0.49!3~-0.32!4~0.14!5~-0.17!6~-0.38!7~0.54!8~-0.13!9~-0.02!f0~31~25',
        '_ga': 'GA1.2.1463121630.1679374474',
        '_gat_UA-147961841-1': '1',
    }

    headers = {
        'authority': 'www.aldoshoes.in',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ta;q=0.8,hi;q=0.7',
        'cache-control': 'no-cache',
        # 'cookie': 'dwanonymous_5b1426a9b1add3e91ed7230c2c4c5c66=cfxgKdthCHOaebA45Ibr0LqSEc; __cq_uuid=cdESI4NmcINb76d5RZlFoxpaYh; _gac_UA-147961841-1=1.1679374475.EAIaIQobChMItfe7tJ3s_QIVRn8rCh0GnwDNEAAYASAAEgJK4vD_BwE; _gcl_aw=GCL.1679374475.EAIaIQobChMItfe7tJ3s_QIVRn8rCh0GnwDNEAAYASAAEgJK4vD_BwE; _gcl_au=1.1.1525965429.1679374475; _fbp=fb.1.1679374475455.1541884172; _gid=GA1.2.1636619829.1680011119; dwac_099d1b7f0f12b2ec36af62feb3=-D51gYEcxyc1FdOCVMS0aAq97V79I-ejm-I%3D|dw-only|||INR|false|Asia%2FKolkata|true; cqcid=cfxgKdthCHOaebA45Ibr0LqSEc; cquid=||; sid=-D51gYEcxyc1FdOCVMS0aAq97V79I-ejm-I; __cq_dnt=0; dw_dnt=0; dwsid=xBfqFtHq0SKCwYXMZIp66zaUcsmt1fGmLDYuyEClnuHptOgy6E9k2gj5MQO1LKY5UuE0Riccopq1tf01UrfPTw==; _ga_5FDJMYHPK9=GS1.1.1680063880.5.1.1680065161.0.0.0; __cq_bc=%7B%22bgsc-aldo-shoes%22%3A%5B%7B%22id%22%3A%22ZULIAN001%22%7D%2C%7B%22id%22%3A%22REX115043%22%7D%2C%7B%22id%22%3A%22REX001043%22%7D%2C%7B%22id%22%3A%22GENTO001043%22%7D%2C%7B%22id%22%3A%22AERUS271041%22%7D%2C%7B%22id%22%3A%22ACES100043%22%7D%5D%7D; __cq_seg=0~-0.04!1~0.39!2~0.49!3~-0.32!4~0.14!5~-0.17!6~-0.38!7~0.54!8~-0.13!9~-0.02!f0~31~25; _ga=GA1.2.1463121630.1679374474; _gat_UA-147961841-1=1',
        'dnt': '1',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }
    custom_settings =  {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'aldo.csv',
        'FEED_EXPORT_FIELDS': [
                            'product_url',
                            'product_name',
                            'product_id',
                            'product_brand',
                            'mrp',
                            'price',
                            'currency',
                            'product_sizes',
                            'size_country',
                            'importer_address',
                            'image_urls']
                        }

    def parse(self, response):
        sel  = Selector(response)
        sitemap = sel.re_first(r'http.*sitemap.*\.xml')
        yield response.follow(sitemap,callback=self.get_products_url)

    def get_products_url(self,response):
        sel = Selector(response)
        products_url = sel.re_first(r'htt.*product.*\.xml')
        yield response.follow(products_url,callback=self.get_product_urls)

    def get_product_urls(self,response):
        sel = Selector(response)
        product_urls = sel.re(r'http.*footwear.*\.html')
        for url in product_urls:
            yield response.follow(
                url,headers=self.headers,
                cookies=self.cookies,callback=self.parse_details)

    def parse_details(self,response):


        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        def clean_importer(importer_text):
           importer =  re.search('/span>(.*)</p>',importer_text,re.DOTALL).group(1).strip()
           return  importer

        def get_currency(price_string):
            currency = Price.fromstring(price_string)
            return currency.currency

        def get_amount(price_string):
            amount = Price.fromstring(price_string)
            return amount.amount_float

        item = AldoshoesItem()


        item['product_url']=response.url
        try:
            item['product_name'] = extract_with_css(
                'h1[class="product-name product_name_pdp product_name_pdp_md"]::text')
        except:
            item['product_name'] = ''
        try:
            item['product_id'] = extract_with_css('span.product-id::text')
        except:
            item['product_id'] = ''
        try:
            item['product_brand'] = extract_with_css('div[class="product-brand"]::text')
        except:
            item['product_brand'] = ''

        try:
            mrp = response.css(
            'span[class="value"]:contains("reduced from")::text').re(r'.{1,2}\d.*\d')[0]
            item['mrp'] = get_amount(mrp)
        except:
            item ['mrp'] = ''
        try:
            price = response.css(
            'span[class="sales price-checkoutPage"] span::text').re(r'.{1,2}\d.*\d')[0]
            item['price'] = get_amount(price)
            item['currency'] = get_currency(price)
        except:
            item ['price'] =''
            item['currency'] = ''
        try:
            item[ 'product_sizes'] = response.css(
                'button[class="customMadeSelect select-size "]::text').re('\d*\.?\d?\d')
        except:
            item[ 'product_sizes'] = ''
        try:
            item['size_country'] = extract_with_css('label[class="size attributes-heading-name-pdp"]::text')
        except:
            item['size_country'] = ''
        try:
            importer_text = response.css('span:contains("Importer")').xpath('parent::p').get().strip()
        except:
            importer_text = ''
        try:
            item[ 'importer_address'] = clean_importer(importer_text)
        except:
            item[ 'importer_address'] = ''
        try:
            image_relative_links = response.css(
                'div[class="imageThombnilesPDP"] img[src]::attr(src)').getall()
        except:
            image_relative_links =''
        try:
            image_links = [response.urljoin(link) for link in image_relative_links]
            item['image_urls'] = image_links
        except:
            item['image_urls'] = ''
        yield item

