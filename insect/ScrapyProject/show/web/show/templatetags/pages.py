from django import template
register = template.Library()

# 要输出必须用这个方法
from django.utils.html import format_html

@register.simple_tag
def showpage(count,request):

    # 其他URL参数添加进URL
    kv = ''
    for i in request.GET:
        # 如果传过来的参数是当前页,就不要加进去了
        if i != 'p':
            kv += '&' + i + '=' + request.GET.get(i)

    # 获取当前多少页面,第一打开默认1
    p = request.GET.get('p', 1)

    p = int(p)

    begin = p - 4
    end = p + 5

    if p <= 4:
        begin = 1
        end = 10

    if p >= count - 5:
        begin = count - 10
        end = count

    if count <= 10:
        begin = 1
        end = count

    # 通过循环要显示的页码范围,用字符串拼接的方法,拼接出链接来
    a = ''
    a += '<li ><a href="?p=1' + kv + '"><<</a></li>'

    # 上一页判断,如果是第一页,上一页还是首页
    if p == 1:
        a += '<li ><a href="?p=1' + kv + '"><</a></li>'
    else:
        a += '<li ><a href="?p=' + str(p - 1) + kv + '"><</a></li>'

    for i in range(begin, end + 1):
        if i == p:
            a += '<li class="active" ><a href="?p=' + str(i) + kv + '">' + str(i) + '</a></li>'
        else:
            a += '<li ><a href="?p=' + str(i) + kv + '">' + str(i) + '</a></li>'

    # 下一页判断,如果是最后一页,下一页是还是组后页面
    if p == count:
        a += '<li ><a href="?p=' + str(count) + kv + '">></a></li>'
    else:
        a += '<li ><a href="?p=' + str(p + 1) + kv + '">></a></li>'
    a += '<li ><a href="?p=' + str(count) + kv + '">>></a></li>'

    return format_html(a)