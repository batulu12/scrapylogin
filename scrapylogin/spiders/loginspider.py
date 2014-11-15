import scrapy
class loginspider(scrapy.Spider):
    name = 'lgsm'
    start_urls = ['http://www.newsmth.net/nForum/#!mainpage']
    def parse(self, response):
        return scrapy.FormRequest.from_response(
                response,
                formdata={'id': 'batulu12', 'passwd' : 'hshy12'},
                callback=self.after_login
                )

    def after_login(self, response):
        # check login succeed before going on
        #if "authentication failed" in response.body:
        #    self.log("Login failed", level =log.ERROR)
        #return
        # continue scraping with authenticated session...
        f = open('C:\code\scrapy\scrapylogin\scrapylogin\login.html','w')
        f.write(response.body)
        f.close()
