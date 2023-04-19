# challenge faced
## dynamic site :
after i got the category urls i sent requests to each of them but they showed me one page but in the top left corner there was product count which was more than i saw in the page so i scrolled up the page was dynamically loaded 
so i decided to use selenium along with requests using selenium i scrolled to bottom of the page and waited for page to load all the pages 
## about the script
script does simple thing it gets the category urls using the get_division_links method and calls get_product_urls this method gets all the product urls byt paginating all the pages using selenium
then work goes to parse details method it parses all the required data then all the data saved in to csv using the save_csv method that'it.
