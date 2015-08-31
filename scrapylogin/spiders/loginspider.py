import scrapy
class loginspider(scrapy.Spider):
    name = 'lgsm'
    start_urls = ['http://www.newsmth.net/nForum/?_escaped_fragment_=mainpage']
    def parse(self, response):
        return scrapy.FormRequest.from_response(
                response,
                formdata={'u_login_id': '*******', 'u_login_passwd' : '*******'},
                callback=self.after_login
                )

    def after_login(self, response):
        # check lo before going on
        #if "authentication failed" in response.body:
        #    self.log("Login failed", level =log.ERROR)
        #return
        # continue scraping with authenticated session...
        f = open('C:\code\scrapy\scrapylogin\scrapylogin\login.html','w')
        f.write(response.body)
        f.close()
