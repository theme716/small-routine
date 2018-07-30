#定义
'''
抽象类：具有抽象方法的类就是抽象类
抽象方法：没有方法内容的方法就是抽象方法
作用：指定开发内容的规范，方便协同开发！
'''

#语法
#抽象类：至少里面有一个抽象方法，抽象方法里面不允许有其他东西


#导入抽象类的模块
import abc  #abcstract class
class User(metaclass = abc.ABCMeta):#指定制作抽象类的材料 （元类）
    #属性
    id = 250

    #添加用户操作（绑定类的方法）--->佳蕊
    @abc.abstractmethod
    def add():
        pass

    #删除用户操作（类方法）--->中举
    @abc.abstractclassmethod
    def dele(cls):
        pass

    #修改用户操作（对象方法）--->小丽
    @abc.abstractmethod
    def modi(self):
        pass

    #查找用户操作（静态方法）--->婷婷
    @abc.abstractstaticmethod
    def find():
        pass

    #获取用户名（正常方法）--->从浩
    def getname(self):
        print('获取用户的名称')

#抽象类不能直接使用，没法实例化
#User()
#抽象类的作用是被其他类继承使用

#佳蕊 -->类文件
class JRuser(User):
    #添加用户（绑定类的方法）--->佳蕊
    def add():
        print('佳蕊完成额添加用户操作！')

#中举 -->类文件
class ZJuser(JRuser):
    #删除用户（类方法）
    @classmethod
    def dele(cls):
        print('中举王城的删除用户操作')

#小丽 -->类文件
class ZLuser(ZJuser):
    #修改用户（对象方法）
    def modi(self):
        print('小丽完成的修改用户操作！')

#婷婷-->文件
class TTuser(ZLuser):
    #查找用户（静态方法）-->查找
    @staticmethod
    def find():
        print('婷婷完成了查找用户方法')

#项目开发完毕
#实例化对象
u = TTuser()#只有四个部分层层继承，都完成了，才能实例化，且只能实例化最后一个文件，之前的都是类文件
#调用方法
TTuser.add()
TTuser.dele()
u.modi()
u.find()
u.getname()