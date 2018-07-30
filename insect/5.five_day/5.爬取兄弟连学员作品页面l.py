from lxml import etree
import requests,json


def all_url():
    base_url = 'http://www.itxdl.cn/html/php/phparticles/'
    response = requests.get(base_url)
    response.encoding = response.apparent_encoding
    data = response.text
    html = etree.HTML(data)
    all_url = html.xpath('//*[@class="php_zuopin_fenlei"]//a/@href')
    return all_url

def rep(url):
    print(url)
    print('==========================')
    base_url = url
    # base_url = 'http://www.itxdl.cn/html/java/javaarticles/'
    dict_key = base_url.split('/')[-3]
    list_var = []
    response = requests.get(base_url)
    response.encoding = response.apparent_encoding
    data = response.text
    html = etree.HTML(data)
    info_list = html.xpath('//div[@class="php_xueyuanzuopin_liebiao"]')
    if info_list:
        for info in info_list:
            if info.xpath('.//p[3]/text()'):
                a = info.xpath('.//p[3]/text()')[0]
            else:
                a = ''
            info_dict = {
                "obj_name": info.xpath('.//p[1]/text()')[0],
                "obj_cla": info.xpath('.//p[2]/text()')[0],
                "obj_user":a,
                "obj_info": info.xpath('.//p[4]//a/text()')[0],
                "obj_info_url": info.xpath('.//p[4]//a/@href')[0]
            }
            list_var.append(info_dict)
    dict_var[dict_key] = list_var



if __name__ == '__main__':
    urls = all_url()

    f = open('./json/itxdl.json','w',encoding='utf-8')
    dict_var = {}
    for url in urls:
        rep(url)
    f.write(json.dumps(dict_var,ensure_ascii=False))
    f.close()


