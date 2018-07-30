from urllib import request,parse

base_url = 'https://weibo.com/u/2934524783/home'
# 构建请求头
headers = {
    'Cookie': 'SINAGLOBAL=6073065172809.875.1526908858549; YF-Ugrow-G0=57484c7c1ded49566c905773d5d00f82; login_sid_t=c5ab32cf9e8256d9416aad0748a659ba; cross_origin_proto=SSL; YF-V5-G0=c99031715427fe982b79bf287ae448f6; WBStorage=5548c0baa42e6f3d|undefined; _s_tentry=passport.weibo.com; wb_view_log=1366*7681; Apache=4025693914091.5483.1528483527173; ULV=1528483527180:4:2:2:4025693914091.5483.1528483527173:1528077169631; un=ckttty@sina.com; YF-Page-G0=bf52586d49155798180a63302f873b5e; UOR=,,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWoR4eXlhK28yPeHkK4vfnb5JpX5K2hUgL.Foz4e0BfeoBN1he2dJLoIpjLxKnL12qL1-eLxK-LBKBLBoBLxKqLB-BL12et; ALF=1560019805; SSOLoginState=1528483805; SCF=Ahkn8773em3z6InlsAWkJTwD9dqQoBMoIQzNZOG-771MrxAcNIxf0birMjHio5H9UuP9lO1gSWFP5gT9gX3Ngwk.; SUB=_2A252Hr-ODeRhGeRH6FYU8irLwz-IHXVVbZZGrDV8PUNbmtANLWfYkW9NTatCQWA3Co2nm8QMjMinJDDnXutQTVku; SUHB=0wnFw7gi41jNkJ; wvr=6'
}
# 构建请求
req = request.Request(base_url,headers=headers)

# 发送请求
response = request.urlopen(req)

print(response.read().decode())