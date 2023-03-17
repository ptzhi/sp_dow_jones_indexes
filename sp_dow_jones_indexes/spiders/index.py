import scrapy
import json

# IndexId = 92411306 -> broad digital market index
# 1679007411 -> unix timestamp
class SPSpider(scrapy.Spider):
    name = 'index'
    start_urls = [
        'https://www.spglobal.com/spdji/en/util/redesign/index-data/get-performance-data-for-datawidget-redesign.dot?indexId=92411306&language_id=1&_=1679007411'
        ]

    def parse(self, response):
        jsonresponse = json.loads(response.text)
        indexpricedict = jsonresponse['indexLevelsHolder']['indexLevels']
        for i in range(0,len(list(indexpricedict))):
            yield {
                'indexid': indexpricedict[i]['indexId'],
                'dateint': indexpricedict[i]['effectiveDate'],
                'datestr': indexpricedict[i]['formattedEffectiveDate'],
                'indexprice': indexpricedict[i]['indexValue']
            }
        with open("index.json", "w") as outfile:
            json.dump(indexpricedict, outfile)
