'''
#描述符
#掌管成员属性操作的类
class MSF:
    #建立一个代替成员属性的临时属性(稻草人)
    def __init__(self):
        #就是在描述符类种代替username进行操作
        self.var = '张乐'

    #获取成员属性
    def __get__(self,obj,cls):#self 当前描述赋的对象 obj 邮箱对象  cls邮箱类
        #用户名获取的相关处理(隐藏中间文字,只显示开头和结尾)
        result = self.var[0] + '*' +self.var[-1]
        return result

    #设置成员属性
    def __set__(self,obj,value):
        #设置值(可以添加条件,内容的修饰操作)
        self.var = value

    #删除成员属性
    def __delete__(self,obj):
        #通过邮箱对象判断用户名是否允许删除
        if obj.isallowdel == True:
            #将self.var删除 究相当于删除了username
            del self.var
        else:#不允许删除
            pass

class Email:
    #成员属性
    username = MSF()#操作的内容#将用户名交给描述赋的一个[对象]掌管
    password = '12346789'
    #是否允许删除用户名
    isallowdel = False

    #成员方法
    #登录
    def login(self):
        print('登录邮箱!')

    #推出
    def logout(self):
        print('推出登录')

#实例化对象
e = Email()

#获取用户名
#print(e.username)

#设置用户名
#e.username = '小婷婷'
#print(e.username)

#删除用户名
del e.username
print(e.username)

'''



'''
#描述符

#邮箱类/描述赋的内容
class Email:
    # 成员属性
    #username = '匿名用户'
    password = '12346789'
    # 是否允许删除用户名
    isallowdel = False

    # 成员方法
    # 登录
    def login(self):
        print('登录邮箱!')

    # 推出
    def logout(self):
        print('推出登录')

    def __init__(self):
        #设置一个用于在描述赋种管理用户名的映射变量
        self.var = '张科'

    # 获取
    def fget(self):
        #管理获取的相关操作
        return self.var

    # 设置
    def fset(self,value):
        #管理设置操作
        self.var = value

    # 删除
    def fdelete(self):
        #管理删除操作
        del self.var

    #将username交接给描述赋(必须在三个方法之后)
    username = property(fget,fset,fdelete)#必须是 获取,设置,删除的顺序!


#实例化邮箱对象
e = Email()

#获取操作
#print(e.username)

#设置操作
#e.username = '何守猛'
#print(e.username)

#删除操作
del e.username
print(e.username)

'''

'''
#描述符

#描述赋/邮箱类
class Email:
    # 成员属性
    #username = '匿名用户'
    password = '12346789'
    # 是否允许删除用户名
    isallowdel = False

    # 成员方法
    # 登录
    def login(self):
        print('登录邮箱!')

    # 推出
    def logout(self):
        print('推出登录')

    #设置映射变量
    def __init__(self):
        self.var = '小丽'

    #获取操作
    @property#声明当前函数名就是需要管理的属性 #装饰器语法
    def username(self):
        return self.var

    #设置操作
    @username.setter#装饰器语法
    def username(self,value):
        self.var = value

    #删除操作
    @username.deleter#装饰器语法
    def username(self):
        del self.var


#实例化对象
e = Email()

#获取
#print(e.username)

#设置
#e.username = '小于'
#print(e.username)

#删除
del e.username
print(e.username)
'''