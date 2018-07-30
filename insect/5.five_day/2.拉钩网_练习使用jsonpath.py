import requests,json,jsonpath

base_url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
response = requests.get(base_url)
response.encoding = response.apparent_encoding

data = response.text
data = json.loads(data)
ress = jsonpath.jsonpath(data,'$..allCitySearchLabels.*.*')
for res in ress:
    print(res['name'],res['id'])
    print('=============')