# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class ScrapyamazonPipeline(object):
    #def process_item(self,item,spider):
    #    return item        
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('newbooks_amazon.db')
        self.curr = self.conn.cursor()
    
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS new_books_amazon""")
        self.curr.execute("""create table new_books_amazon(
                            book_title text,
                            product_imagelink text,
                            product_author text,
                            price_hardcover text,
                            price_kindle text,
                            price_audible text
                            )""")

    def process_item(self, item, spider):
            self.store_db(item) 
            #print("Pipeline :" + item['product_name'][0])
            return item

    def store_db(self, item):
        self.curr.execute("""insert into new_books_amazon values(?,?,?,?,?,?)""",(
            item['book_title'][0],
            item['product_imagelink'][0],
            ", ".join(str(x) for x in item['product_author']),
            "".join(str(x) for x in item['price_hardcover']),
            "".join(str(x) for x in item['price_kindle']), 
            "".join(str(x) for x in item['price_audible'])
        ))
        self.conn.commit()




