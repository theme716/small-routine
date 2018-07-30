import jsonpath,json

s = '''
{ "store": {
    "book": [ 
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  },
  "taobao":{
        "phone":{
            "name":"apple",
            "color":"jak_black",
            "price":9.99
        }
  }
}
'''
# $ the root object/element
# print(jsonpath.jsonpath(json.loads(s),'$'))  # False $不能单独使用

# .or[]  child operator
# print(jsonpath.jsonpath(json.loads(s),'$[taobao]'))
# print(jsonpath.jsonpath(json.loads(s),'$.taobao'))
#[{'phone': {'name': 'apple', 'color': 'jak_black', 'price': 9.99}}]
# 返回值是一个列表，列表里面是taobao键对应的一个个值

# .. recursive descent.(递归向下取)
res = jsonpath.jsonpath(json.loads(s),'$..')

# * 通配符 wildcard. All objects/elements regardless their names.
# 以下两个效果一样
# * 选取book下面的所有元素
# .. 递归选取所有元素
res = jsonpath.jsonpath(json.loads(s),'$.store.book.*')
res = jsonpath.jsonpath(json.loads(s),'$.store.book[*]')

# [,] 索引选取，[1,4] 表示选取索引为1和4的元素
res = jsonpath.jsonpath(json.loads(s),'$.store.book[1,3]')

#[start:end:step] 包前不包后
res = jsonpath.jsonpath(json.loads(s),'$.store.book[0:4:1]')

# ?() 过滤表达式 选取当前元素下的价格不超过10的元素
res = jsonpath.jsonpath(json.loads(s),'$..book[?(@.price<10)]')
# 过滤出所有当前元素中有isbn元素的元素
res = jsonpath.jsonpath(json.loads(s),'$..book[?(@.isbn)]')
# 选取最后一本书
res = jsonpath.jsonpath(json.loads(s),'$..book[(@.length-1)]')
# res = jsonpath.jsonpath(json.loads(s),'$.store.book[-1]') #索引不支持负数


for i in res:
    print(i)
