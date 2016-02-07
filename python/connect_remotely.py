import pymongo
from pymongo import MongoClient

uri = "mongodb://hackathon_reader:To0305@www.oci-ifo.org:27017/scrapy?authMechanism=MONGODB-CR"
client = MongoClient(uri)
db = client.scrapy    
collection = db.articles
#f = open('data.txt', 'w') #uncomment to save output to file
articles = collection.find({"full_article": {'$regex':'TransCanada'}, "full_article" : { "$exists": 1 }}).limit( 1000 )
for x in articles:
    print x
#    print  >>f, x #uncomment to save output to file

