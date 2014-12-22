from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import FormRequest, Request
from scrapy import log 
class AmazonSpider(CrawlSpider):
    name = 'renren'
    #allowed_domains = ['amazon.cn']
    #allowed_domains = ['zhihu.com']
    allowed_domains = ['renren.com']
    #allowed_domains = ['weibo.com']
    #allowed_domains = ['newsmth.net']
    #start_urls = ['http://associates.amazon.cn/gp/associates/network/main.html']
    #start_urls = ['https://associates.amazon.cn/gp/associates/network/reports/report.html']
    #start_urls = ['http://www.zhihu.com/login']
    start_urls = ['http://www.renren.com/']
    #start_urls = ['http://weibo.com/']
    #start_urls = ['http://www.newsmth.net/nForum/index']
    # username, password,
    def __init__(self, *args, **kwargs):
        super(AmazonSpider, self).__init__(*args, **kwargs)
        self.http_user = 'hshy1987@sina.com'
        self.http_pass = 'hshy1987315'
        #login form
        self.formdata = {
                        'email':self.http_user, \
                        'passward':self.http_pass,\
                        }   
         
        self.headers = {
                       

                       }
        self.cookies = {
                       'jebecookies':'bb3a8c3d-ad66-4724-9adc-fb4f6a8a73ce|||||',
                       'ick_login':'c23f8488-8e07-4390-8211-fc7f0daac788',
                       'loginfrom':'null',
                       'anonymid':'i3z6a791-de2c38',
                       'depovince':'GW',
                       '_r01_':'1',
                       'ln_uact':'hshy1987@sina.com',
                       'ln_hurl':'http://hdn.xnimg.cn/photos/hdn221/20100608/2200/h_main_VO2d_4f38000006962f74.jpg', 
                       '_de':'7A4404662C2F1FF5270E2E3B4A0CA0A66DEBB8C2103DE356',
                       'p':'9ad79e306e7826124349c6a1db8ac3798',
                       'first_login_flag':'1',
                       't':'afb73ff363117269ba6314c2c9d4f0648',
                       'societyguester':'afb73ff363117269ba6314c2c9d4f0648',
                       'id':'221103138',
                       'xnsid':'8f5092fb',
                       'JSESSIONID':'abclA4OKmwzxP_DiGIVPu',
                       'feedType':'221103138_hot'
        }
        self.id = 0 

    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            yield FormRequest(url, meta = {'cookiejar': i},\
                               # formdata = self.formdata,\
                                cookies = self.cookies,\
                                callback = self.login)#jump to login page

    def _log_page(self, response, filename):
        with open(filename, 'w') as f:
            f.write("%s\n%s\n%s\n" % (response.url, response.headers, response.body))
    def login(self, response):
        self._log_page(response, 'renren_login.html')
        return [FormRequest.from_response(response, \
                            formdata = self.formdata,\
                            headers = self.headers,\
                            meta = {'cookiejar':response.meta['cookiejar']},\
                            callback = self.parse_item)]#success login

    def parse_item(self, response):
        self._log_page(response, 'after_login.html')
        hxs = HtmlXPathSelector(response)
        report_urls = hxs.select('//div[@id="menuh"]/ul/li[4]/div//a/@href').extract()
        for report_url in report_urls:
            #print "list:"+report_url
            yield Request(self._ab_path(response, report_url),\
                            headers = self.headers,\
                            meta = {'cookiejar':response.meta['cookiejar'],\
                                    },\
                            callback = self.parse_report)

    def parse_report(self, response):
        self.id = self.id + 1
        self._log_page(response, "%d.html" %self.id)