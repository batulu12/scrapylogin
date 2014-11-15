# -*- coding: utf-8 -*-

# Scrapy settings for scrapylogin project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapylogin'

SPIDER_MODULES = ['scrapylogin.spiders']
NEWSPIDER_MODULE = 'scrapylogin.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapylogin (+http://www.yourdomain.com)'

LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_FILE = 'C:\code\scrapy\scrapylogin\scrapylogin\log\login.log'
LOG_LEVEL = 'DEBUG'
LOG_STDOUT = False
