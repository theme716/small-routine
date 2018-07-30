#装饰器：

#第一步：基本函数
'''
def xxoo():
    print('AAAAAA')

#调用函数
xxoo()
xxoo()
'''


#第二部：功能拓展
'''
#扩展功能的函数
def description(func):#func接收基本函数 func = xxoo
    #功能扩展1
    print('脱衣服')
    #基本功能
    func()
    #功能扩展2
    print('互相拥抱')

#基本函数
def xxoo():
    print('xxoo')

xxoo = description(xxoo)
#调用函数
#xxoo()  #由于装饰器函数现在没有返回值，所以无法调用，xxoo现在是None
'''


#第三部：装饰器原理
'''
#扩展功能的函数
def description(func):#func接收基本函数 func = xxoo
    #内部函数
    def inner():
        #功能扩展1
        print('脱衣服')
        #基本功能
        func()
        #功能扩展2
        print('互相拥抱')
    #返回内部函数
    return inner #千万别写成inner()

#基本函数
def xxoo():
    print('xxoo')

#要求： xxoo函数功能扩展后依然要是xxoo函数
xxoo = description(xxoo)#返回值需要是一个函数 相当于a = a + a 1
print('---------------')
#调用函数
xxoo()
'''


#第四部：实现基本的装饰器(语法糖)
'''
#扩展功能的函数
def description(func):#func接收基本函数
    #内部函数
    def inner():
        #功能扩展1
        print('脱衣服')
        #基本功能
        func()
        #功能扩展2
        print('互相拥抱')
    #返回内部函数
    return inner

@description
#基本函数
def xxoo():
    print('xxoo')

print('---------------')
#调用函数
xxoo()
'''


#第五步：带有参数和返回值的基本函数
'''
#带有参数的函数
def description(func):#这里相当于是 xxoo(who,time)
    #制作内部函数
    def inner(w,t):
        #扩展功能1
        print('脱衣服')
        #基本函数
        func(w,t)#这里相当于使用调用func函数，传入的实参是w,t
        #扩展功能2
        print('互相拥抱')
    return inner

@description
def xxoo(who,time):
    print(who,'这是基本函数的内容',time)

xxoo('111111','2222222')
#调用xxoo函数，相当于调用inner函数，
# 1111,2222是传入的实参，被inner的形参w,t分别接收。
#func()函数使用时，使用了inner的参数，即func(w,t)
'''
'''
#带有返回值的函数
def description(func):
    #制作内部函数
    def inner():
        #扩展功能1
        print('脱衣服')
        #基本函数
        result = func()
        #扩展功能2
        print('互相拥抱')
        #添加返回值（xxoo的返回值）
        return result
    return inner

@description
def xxoo():
    print('这是基本函数的内容')
    return '这是基本函数里面的返回值'

jp = xxoo()
print('-------------------')
print(jp)
'''


#第六步：带有收集参数的函数
'''
def description(func):
    #制作内部函数
    def inner(*t,**p):
        #扩展功能1
        print('脱衣服')
        #基本函数
        func(*t,**p)
        #扩展功能2
        print('互相拥抱')
    return inner

@description
def xxoo(*tool,**price):
    print('购买了工具',tool)
    print('花费了费用',price)
    print('这是基本函数的内容')

#调用基本函数
xxoo('皮鞭','蜡烛','小木棍',pibian = '20',lazhu = '10',xiaomugun = '0')
'''

#第七部：带有参数的装饰器
'''
#让一个装饰器装饰好几个函数
#声明装饰器
def outer(arg):
    def description(func):
        def inner():#扩展拉屎
            print('脱裤子')
            func()
            print('穿裤子')

        def inner2():#扩展仨鸟
            print('拉苦练')
            func()
            print('光裤链')

        if arg == 'la':#返回内部函数
            return inner#更具outer的参数判断返回哪个结果
        elif arg == 'sa':
            return inner2
    #outer的返回值是装饰器
    return description

#基本函数1
@outer('la')
def lashi():
    print('砰砰砰')

#基本函数2
@outer('sa')
def saniao():
    print('嘘嘘嘘哗啦啦')

lashi()
print('--------------------------------')
saniao()
'''

#第八步： 将类当做参数传入装饰器
'''
#扩展功能已经存在于某个类中
class Action:
    #绑定类的方法
    def start():
        print('绑定类方法第一个')
    def end():
        print('绑定类方法第二个')

#装饰器
def outer(cls):
    def description(func):
        def inner():  # 扩展拉屎
            cls.start()
            func()
            cls.end()
        return inner
    return description

@outer(Action)
def xxoo():
    print('这是基本函数的内容')

xxoo()
'''


#第九步：使用类作为装饰器（实际上是使用类中的方法作为装饰器）
'''
class Sleep:

    #外层函数
    def __init__(self,arg):
        #print(arg)
        #如果有参数就存入对象方便其他方法使用
        self.arg = arg

    #装饰器函数
    def __call__(self,func):
        #将基本函数存入对象
        self.func = func
        return self.inner
    #未来的inner函数的方法
    def inner(self):
        print('洗澡澡')
        self.func()
        print('睡觉觉')

@Sleep('la') #Sleep()相当于@对象
def xxoo():
    print('这是基本函数的内容')
xxoo()
'''


#第十步：为类添加装饰
'''
def description(cls):
    def inner():
        obj = cls()
        obj.no = '1111111'
        return obj
    return inner

@description
class Human:
    #属性
    age = 0
    color = 'yellow'
    #方法
    def cry(self):
        print('yingyingying')
    def smile(self):
        print('wuwuwuwuwu')

jr = Human()
print(jr.__dict__)
'''


#第十一步:装饰器的嵌套
def descr1(func):
    def inner():
        print('第一个装饰器的扩展功能')
        func()
        print('第一个装饰器结束')
    return inner
def descr2(func):
    def inner():
        print('第二个装饰器扩展功能')
        func()
        print('第二个装饰器结束')
    return inner

@descr1
@descr2
def xxoo():
    print('xxoo')
xxoo()