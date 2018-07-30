from lxml import etree

data = etree.parse('data.xml') #<lxml.etree._ElementTree object at 0x00000162391F4608>


# /text() 输出某元素的内容
res = data.xpath('/bookstore/book[1]/price/text()')
# /@lang 输出某元素的lang属性的值
res = data.xpath('//title/@lang') #['eng', 'cn', 'cn']



# 路径表达式语法
# 1、/ 从根节点选取 相当于jsonpath中的$
res = data.xpath('/bookstore')
# 2、// 相当于jsonpath中的.. 从当前节点递归乡下选取
res = data.xpath('//bookstore')
# 3、. 选取当前节点 相当于jsonpath中的@
res = data.xpath('.')
# 4、.. 当前节点的父节点
# 5、@ 选取属性
# 所有title元素的所有lang属性
res = data.xpath('//title/@lang') #['eng', 'cn', 'cn']




# 谓语（Predicates）谓语用来查找某个特定的节点或者包含某个指定的值的节点。
# 谓语被嵌在方括号中。

#选取属于 bookstore 子元素的第一个 book 元素。
# [索引]---从1开始
res = data.xpath('/bookstore/book[1]/price/text()')
# [last()]选取最后一个元素
res = data.xpath('/bookstore/book[last()]/price/text()')
# [last()-1] 选取倒数第二个元素
res = data.xpath('/bookstore/book[last()-1]/price/text()')
# [position()<3] 选取前两个元素
res = data.xpath('/bookstore/book[position()<3]/price/text()')
# 选取拥有lang属性的所有title元素的lang属性的值
res = data.xpath('//title[@lang]/@lang')
# 选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。
res = data.xpath('//title[@lang="eng"]/@lang')
# 选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。
res = data.xpath('/bookstore/book[price>35]')
# 选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。
res = data.xpath('/bookstore/book[price>35]/title/text()')


# 选取未知节点
# * 匹配任何元素节点
res = data.xpath('/bookstore/*//text()') #选取 bookstore 元素的所有子元素。
# @* 匹配任何属性节点
res = data.xpath('//title[@*]/text()')


# 选取若干路径
# 选取 book 元素的所有 title 和 price 元素的内容
res = data.xpath('//book/title/text() | //book/price/text()')
# 选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素。
res = data.xpath('/bookstore/book/title | //price')

print(res)