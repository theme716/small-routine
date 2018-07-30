from lxml import etree

html = '''
<bookstore> 
  <book price="100" category="cooking"> 
    <title lang="en">Everyday Italian</title>  
    <author>Giada De Laurentiis</author>  
    <year>2005</year>  
    <price>30.00</price> 
  </book>  

  <book category="children"> 
    <title lang="en">Harry Potter</title>  
    <author>J K. Rowling</author>  
    <year>2005</year>  
    <price>29.99</price> 
  </book>  

  <book category="web"> 
    <title category="web">XQuery Kick Start</title>  
    <author>James McGovern</author>  
    <author>Per Bothner</author>  
    <author>Kurt Cagle</author>  
    <author>James Linn</author>  
    <author>Vaidyanathan Nagarajan</author>  
    <year>2003</year>  
    <price>49.99</price> 
  </book> 

  <book category="web" cover="paperback"> 
    <title>Learning XML</title>  
    <author>Erik T. Ray</author>  
    <year>2003</year>  
    <price>39.95</price> 
  </book> 

  <book> 
    <title>Learning Python</title>  
    <author>Erik T. Ray</author>  
    <year>2003</year>  
    <price>20000</price> 
  </book> 
</bookstore>
'''

html = etree.HTML(html)

# res = html.xpath('//book/@cover | //book/@category ')
# res = html.xpath('//book//*')
# res = html.xpath('//book[@*]/title/text()')
# res = html.xpath('//*[@category="web"]')
# res = html.xpath('//book/../../*')

# print(res)



