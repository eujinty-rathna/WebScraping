# scraping the hipstore ecommerce site

## libraries used
- requests
- BeautifulSoup
- pandas 
- re
- price_parser
- urllib

## what we do in the script 
we have created the class name hipstore in order by having several method each method is 
kind of rule to scrape the website using some techniques

## hipstore class
hipstore class has several methods they are 
-__init__ 
- start_request 
- get_product_urls 
- pagination
- parse_details
- get_symbol
- get_amount 
- save_csv
- crawl

### __init__ :
we are initilizing the class attributes in order to ease the method use of the attributes
here we are initilizing the headers , cookies , url and somether containers to store scraped data like 
data_list and product_urls

### start_request:
 this method sends the initial request to the targeted website and gets the page soure and then gets the 
 category urls by parsing using parsing libray
 
### get_product_urls:
this method iterates over all the category and gets the each product url and then using pagination fucntion
in order to paginate to all the pages 

### parse_details :
this method parses all the details we need for further analysis 
like 
- price
- brand 
- colors
- sizes
- product name 
- size country 
- currency symbol

this product uses two mini function in order to get  price in float and currey symbols  in further we used 
re module to get the product sizes from the country name and country form the product sizes

### save_csv:
this methods saves the all data in to csv

### crawl:
this is the method which starts the crawling process 
