import scrapy
from ..items import ScrapyamazonItem
from scrapy.utils.response import open_in_browser

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    page_number = 2
    start_urls = ["https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011"]
    
    def parse(self, response):
        #if not hxs.select('//get/site/logo'):
        #    yield Request(url=response.url, dont_filter=True)

        open_in_browser(response)

        for section in response.css('div.s-main-slot>div.sg-col-20-of-24.s-result-item.s-asin.sg-col-0-of-12'):           
            book_title = section.css('span.a-size-medium.a-color-base.a-text-normal::text').extract()
            product_imagelink = section.css('div.a-section.aok-relative.s-image-fixed-height>img::attr(src)').extract()
            price_hardcover = section.xpath(".//div[./a[contains(text(),'Hardcover')]]/following-sibling::div//span[contains(@class,'a-offscreen')]/text()").get()
            price_kindle = section.xpath(".//div[./a[contains(text(),'Kindle')]]/following-sibling::div//span[contains(@class,'a-offscreen')]/text()").get()
            price_audible = section.xpath(".//div[./a[contains(text(),'Audible')]]/following-sibling::div//span[contains(@class,'a-offscreen')]/text()").get(default='unavailable')
            product_author_x = section.xpath(".//div[contains(@class,'a-row a-size-base a-color-secondary')]//span[contains(text(),'by')]")
            product_author = []      
            for value in product_author_x.xpath("./following-sibling::*[contains(@class,'a-size-base') and not(text()=' and ')]/text()").getall():
                product_author.append(" ".join(value.split()))

            items = ScrapyamazonItem()
            items['book_title'] = book_title
            items['price_hardcover'] = price_hardcover
            items['price_kindle'] = price_kindle
            items['price_audible'] = price_audible
            items['product_imagelink'] = product_imagelink

            if '|' in product_author:
                items['product_author'] = product_author[:-2]
            else:
                items['product_author'] = product_author

            yield items

        next_page = "https://www.amazon.com/Books-Last-30-days/s?i=stripbooks&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&page="+str(AmazonSpiderSpider.page_number)+"&qid=1603647684&ref=sr_pg_"+str(AmazonSpiderSpider.page_number)
        if AmazonSpiderSpider.page_number <=2:
            AmazonSpiderSpider.page_number+=1
            yield response.follow(next_page,callback=self.parse)


