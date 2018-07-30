from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import ZhaoPin

def index(request):

    data = ZhaoPin.objects.all()
    # context = {'data':data}
    # 载入分页模块
    from django.core.paginator import Paginator
    # 实例化分页类，创建一个分页对象
    paginator = Paginator(data,10)
    # 获取总页数
    num = paginator.page_range

    p = request.GET.get('p',1)
    onepage = paginator.page(p)

    context = {'data':onepage,'num':num}
    return render(request,'index.html',context)


