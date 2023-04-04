'''importing required modules'''
import re
from aldoshoes.items import AldoshoesItem
import scrapy
from scrapy.selector import Selector
from price_parser import  Price

class AldoSpider(scrapy.Spider):
    '''AldoSpider is about to get the footwear product
    details from the wwww.aldoshoes.in ... since we
    could get all the proudct information from the sitemap
    and they are up to date we are approching it.'''

    name = "aldo"
    start_urls = ["https://www.aldoshoes.in/robots.txt"]
    cookies = {
        'dwanonymous_5b1426a9b1add3e91ed7230c2c4c5c66': 'abl2PVsDLXYCY6ULdmR5P4iT7U',
        '__cq_uuid': 'abl2PVsDLXYCY6ULdmR5P4iT7U',
        '__cq_bc': '%7B%22bgsc-aldo-shoes%22%3A%5B%7B%22id%22%3A%22REX115043%22%7D%5D%7D',
        '_gcl_au': '1.1.363859448.1679390359',
        '_fbp': 'fb.1.1679390359914.197674320',
        'dwac_099d1b7f0f12b2ec36af62feb3': 'CgUIW_iJbnUZ72Coao6RNI6F0YTeyyyp_aY%3D|dw-only|||INR|false|Asia%2FKolkata|true',
        'cqcid': 'abl2PVsDLXYCY6ULdmR5P4iT7U',
        'cquid': '||',
        'sid': 'CgUIW_iJbnUZ72Coao6RNI6F0YTeyyyp_aY',
        '__cq_dnt': '0',
        'dw_dnt': '0',
        'dwsid': 'p93E4xVh7CMVFhhj2A7m7CNdHTwzI67_8V_Nb1-SlZAkK5z4l1NL39ycONG5_rDHNsu2igiCfyYganzPR3brYA==',
        'rtb-global': '9d87ee13-f26f-4d13-b81c-1a0ca53d1996',
        '_gid': 'GA1.2.990423684.1680602721',
        '_gac_UA-147961841-1': '1.1680602721.Cj0KCQjwla-hBhD7ARIsAM9tQKtEN560D3gmhKt1Ehrl-O045wramUh8IQgj_AJR9wySGfI5lyfbt4MaAinbEALw_wcB',
        '_gcl_aw': 'GCL.1680602723.Cj0KCQjwla-hBhD7ARIsAM9tQKtEN560D3gmhKt1Ehrl-O045wramUh8IQgj_AJR9wySGfI5lyfbt4MaAinbEALw_wcB',
        '_gat_UA-147961841-1': '1',
        '__cq_seg': '0~-0.17!1~0.36!2~0.18!3~-0.70!4~-0.30!5~-0.20!6~-0.01!7~-0.25!8~-0.15!9~0.30',
        '_ga_5FDJMYHPK9': 'GS1.1.1680605070.3.1.1680605094.0.0.0',
        '_ga': 'GA1.2.1377814464.1679390358',
    }

    headers = {
        'authority': 'www.aldoshoes.in',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'dwanonymous_5b1426a9b1add3e91ed7230c2c4c5c66=abl2PVsDLXYCY6ULdmR5P4iT7U; __cq_uuid=abl2PVsDLXYCY6ULdmR5P4iT7U; __cq_bc=%7B%22bgsc-aldo-shoes%22%3A%5B%7B%22id%22%3A%22REX115043%22%7D%5D%7D; _gcl_au=1.1.363859448.1679390359; _fbp=fb.1.1679390359914.197674320; dwac_099d1b7f0f12b2ec36af62feb3=CgUIW_iJbnUZ72Coao6RNI6F0YTeyyyp_aY%3D|dw-only|||INR|false|Asia%2FKolkata|true; cqcid=abl2PVsDLXYCY6ULdmR5P4iT7U; cquid=||; sid=CgUIW_iJbnUZ72Coao6RNI6F0YTeyyyp_aY; __cq_dnt=0; dw_dnt=0; dwsid=p93E4xVh7CMVFhhj2A7m7CNdHTwzI67_8V_Nb1-SlZAkK5z4l1NL39ycONG5_rDHNsu2igiCfyYganzPR3brYA==; rtb-global=9d87ee13-f26f-4d13-b81c-1a0ca53d1996; _gid=GA1.2.990423684.1680602721; _gac_UA-147961841-1=1.1680602721.Cj0KCQjwla-hBhD7ARIsAM9tQKtEN560D3gmhKt1Ehrl-O045wramUh8IQgj_AJR9wySGfI5lyfbt4MaAinbEALw_wcB; _gcl_aw=GCL.1680602723.Cj0KCQjwla-hBhD7ARIsAM9tQKtEN560D3gmhKt1Ehrl-O045wramUh8IQgj_AJR9wySGfI5lyfbt4MaAinbEALw_wcB; _gat_UA-147961841-1=1; __cq_seg=0~-0.17!1~0.36!2~0.18!3~-0.70!4~-0.30!5~-0.20!6~-0.01!7~-0.25!8~-0.15!9~0.30; _ga_5FDJMYHPK9=GS1.1.1680605070.3.1.1680605094.0.0.0; _ga=GA1.2.1377814464.1679390358',
        'pragma': 'no-cache',
        'referer': 'https://www.aldoshoes.in/handbags/men/backpack/',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }
    # this method to parse the sitemap url from the robots.txt file
    def parse(self, response):
        sel  = Selector(response)
        sitemap = sel.re_first(r'http.*sitemap.*\.xml')
        yield response.follow(sitemap,callback=self.get_products_url)

    # this method is to get the products page url where we could find
    # all the proudcts
    def get_products_url(self,response):
        sel = Selector(response)
        products_url = sel.re_first(r'htt.*product.*\.xml')
        yield response.follow(products_url,callback=self.get_product_urls)

    # this method is about to get the all products url from the proudcts page
    def get_product_urls(self,response):
        sel = Selector(response)
        product_urls = sel.re(r'http.*footwear.*\.html')
        for url in product_urls:
            yield response.follow(
                url,headers=self.headers,
                cookies=self.cookies,callback=self.parse_details)

    # here we are getting our need information by parsing appropriate elements
    def parse_details(self,response):

        # this method is to get simplify our work
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        # this method is to clean the importer details to get quality information
        def clean_importer(importer_text):
           importer =  re.search('/span>(.*)</p>',importer_text,re.DOTALL).group(1).strip()
           importer = importer if importer else ''
           return  importer

        #this method will split the currecy symbol from the price string and return us
        def get_currency(price_string):
            currency = Price.fromstring(price_string)
            return currency.currency

        # this method is to get the price amount from the price string without the currency symbol
        def get_amount(price_string):
            amount = Price.fromstring(price_string)
            return amount.amount_float

        item = AldoshoesItem() # creating item object which we imported from our items.py


        item['product_url']=response.url
        item['product_name'] = extract_with_css(
                'h1[class="product-name product_name_pdp product_name_pdp_md"]::text')

        item['product_id'] = extract_with_css('span.product-id::text')

        item['product_brand'] = extract_with_css('div[class="product-brand"]::text')

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

        item[ 'product_sizes'] = response.css(
                'button[class="customMadeSelect select-size "]::text').re('\d*\.?\d?\d')
        item['size_country'] = extract_with_css('label[class="size attributes-heading-name-pdp"]::text')
        try:
            importer_text = response.css('span:contains("Importer")').xpath('parent::p').get(default='').strip()
            item['importer_address'] = clean_importer(importer_text)
        except:
            item['importer_address'] = ''

        image_relative_links = response.css(
                'div[class="imageThombnilesPDP"] img[src]::attr(src)').getall()
        if image_relative_links:
            item['image_urls'] = [response.urljoin(link) for link in image_relative_links]

        yield item

