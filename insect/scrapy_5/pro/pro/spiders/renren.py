import scrapy

class RenRen(scrapy.Spider):

    name = 'renren'
    custom_settings = {
        'COOKIES_ENABLED':True,
        # '是否启用cookies middleware。如果关闭，cookies将不会发送给web server。'
        # 一般自己设置cookie时候，需要关闭，这样子才能自己设置成功
        # cookie会自动保存cookie,然后在下次请求的时候发出去
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }

    # 自定义首次登陆
    def start_requests(self):
        login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018561626292'
        form = {
            'email':'18609815765',
            'password':'950613ck'
        }
        yield scrapy.FormRequest(url=login_url,headers=self.headers,formdata=form,callback=self.parse_login)


    def parse_login(self,response):
        print('====================1=====================')
        print(response.request.headers)
        print(response.text)
        # print(response.request.headers['Cookie']) #第一次发送的时候没有cookie

        url = 'http://www.renren.com/562409386'
        yield scrapy.Request(url=url,callback=self.home)

    def home(self,response):
        print('========================2==================')
        print(response.text)
        print(response.request.headers['Cookie']) #第二次发送获得了第一次发送response中的cookie
