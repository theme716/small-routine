from urllib import request
import re,os,json

base_url = 'http://www.xicidaili.com/nn/{}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}


if os.path.exists('xici.json'):
    os.remove('xici.json')
f = open('xici.json', 'a', encoding='utf-8')
f.write('[\n')
start = int(input('请输入起始页：'))
end = int(input('请输入结束页：'))
for i in range(start,end+1):
    try:
        full_url = base_url.format(i)
        req = request.Request(full_url,headers=headers)
        response = request.urlopen(req)
        html = response.read().decode()

        tr_pat = re.compile(r'<tr.+?</tr>',re.S)
        trs = tr_pat.findall(html)
        trs=trs[1:]
        first = 0
        last = len(trs)
        for x in range(first,last):
            td_pat = re.compile(r'<td>(.+?)</td>',re.S)
            tds = td_pat.findall(trs[x])
            # 处理一下地区列表里面的索引2
            a_pat = re.compile(r'<a href=.+?>(.+?)</a>')
            tds[2] = a_pat.search(tds[2]).group(1)
            print(tds)
            # # 将数据重组成json格式
            # for x in range(0, len()):

            dict_var = dict(zip(('ip', '端口号', '代理位置', '代理类型', '存活时长','验证时间'), tds))

            # f.write(json.dumps(dict_var, ensure_ascii=False) + ',\n')

            # # 将每个字典后面加逗号和换行符，如果是最后一个字典，则不添加逗号
            if i == end and x == (last - 1):
                f.write(json.dumps(dict_var, ensure_ascii=False) + '\n')
            else:
                f.write(json.dumps(dict_var, ensure_ascii=False) + ',\n')

    except Exception as e:
        print(e)

f.write(']')
f.close()



