from bs4 import BeautifulSoup
import re

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" id="p1"><b>The Dormouse's story</b><b>----2b</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span><b>Elsie</b></span></span>--alice</span></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story" id="p3">...</p>
<div>我是div</div>
'''

# 指定解析器，解析代码
html = BeautifulSoup(html,'lxml')

# 输出格式化之后的dom文档
# print(html.prettify())


# 获取标签
# print(html.a) #只会获取一个

# 标签名称
# print(html.title.name) #获取标签的名称（title/p/a/table）
# print(html.title.string) #获取标签的内容
# print(html.p.string)
# print(html.p.text)  #string 和 text 的区别是：string不支持嵌套的文本，即如果文本在p标签里面的b标签里面，不能获取内容，返回none；而text支持嵌套文本
# print(html.p.b.string) #b标签里面有内容，可以获取

# 获取单个属性
# print(html.p['id']) #p1
# print(html.p['class']) #['title'] 为什么会这样

# 获取所有属性
# print(html.p.attrs)  #{'class': ['title'], 'id': 'p1'}

# 获取指定标签下的所有文本
# print(html.p.get_text())  #  The Dormouse's story----2b(两个b标签的文本连在一起了)





# find---搜索一个元素
# print(html.find(id='link3'))
# print(html.find(href='http://example.com/tillie'))


# find_all  选择多个元素，返回列表（可以进行筛选）
# p_list = html.find_all('p') #输入字符串
# p_list = html.find_all(re.compile('^b')) #输入正则规则
# p_list = html.find_all(["p","div"])
# for p in p_list:
#     print(p)   #返回每一个p元素
    # print(p.get_text()) #继续调用bs4的方法，返回每一个p标签下的所有内容
    # pass

# p_list2 = html.find_all('p',attrs={'class':'title'})
# p_list2 = html.find_all('p',attrs={"id":["p1","p3"]})
# print(p_list2)















# = =====================================select=======================================
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title story1" id="p1"><a><b class="b1">The Dormouse's story</b></a><b>----2b</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span><b>Elsie</b></span></span>--alice</span></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story2" id="p3">...</p>
<div>我是div</div>
'''

html = BeautifulSoup(html,'lxml')

# select 返回值总是一个列表

# 类选择器
# print(html.select('.title'))

# 元素选择器 （html.p返回第一个p元素，select("p")返回所有的p元素组成的列表）
# print(html.select('p'))

# 类选择器结合元素选择器
# print(html.select("p.title"))

# 后代选择器
# print(html.select("p .b1"))

# 子类选择器
# print(html.select("p > .b1")) #必须有空格

# id选择器
# print(html.select("p#p3"))

# 并列选择器
# print(html.select("p.story1,p.story2"))

# 属性选择器
# print(html.select("p[id='p1']"))
# print(html.select('p[class="story2"]'))
# print(html.setect('p[class="$story1"]')) #以什么什么结尾
# print(html.select('p[class^="title st"]')) #以什么什么开头
# print(html.select('p[class*="story"]')) #模糊搜索
