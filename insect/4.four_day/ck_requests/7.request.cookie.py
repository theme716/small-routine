import requests

# 创建一个会话(和urllib里面的opener有点像)
session = requests.session()

def login():
    login_url = 'http://www.renren.com/ajaxLogin/login?1=1'
    data = {
        'email':'18609815765',
        'password':'950613ck'
    }
    response = session.post(login_url,data=data)
    print(response.status_code)

def get_home():
    home_url = 'http://www.renren.com/562409386'
    response = session.get(home_url)
    response.encoding = response.apparent_encoding
    print(response.status_code)
    print(response.text)

if __name__ == '__main__':
    login()
    get_home()


