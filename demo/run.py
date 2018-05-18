import sys
import os
import time
#from scrapy.cmdline import execute

from scrapy import cmdline
#cmdline.execute("scrapy crawl meiju".split())
#cmdline.execute("scrapy crawl xiaohua".split())
#cmdline.execute("scrapy crawl dongguan".split())
#cmdline.execute("scrapy crawl dongguanspider".split())
#cmdline.execute("scrapy crawl kuaidaili".split())
#cmdline.execute("scrapy crawl douban".split())
#cmdline.execute("scrapy crawl patent".split())
#cmdline.execute("scrapy crawl sinaFinance".split())
#cmdline.execute("scrapy crawl yiCaiFinance".split())
#cmdline.execute("scrapy crawl wallStreet".split())
#cmdline.execute("scrapy crawl wallStreetJson".split())
#cmdline.execute("scrapy crawl cnfol".split())
#cmdline.execute("scrapy crawl cnfolJson".split())
#cmdline.execute("scrapy crawl sougou".split())
#cmdline.execute(['scrapy','crawl','sougou'],['scrapy','crawl','sougou1'])

#os.system("scrapy crawl wallStreetJson")
#time.sleep(300)
#os.system("scrapy crawl sougou1")
cmdline.execute("scrapy crawl cjw".split())