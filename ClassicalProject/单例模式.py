#单例设计模式:一个类只能实例化一个对象

print('========================浩哥讲的单例模式====================')

class Zhongju:
    #属性
    sex = '女'
    age = 19
    size = '36G'
    obj = None#未来存储对象的成员属性

    #方法
    #需要new魔术方法
    def __new__(cls):
        # 第一次制作对象
        if cls.obj == None:
            obj = object.__new__(cls)
            #将当前对象存入类种
            cls.obj = obj
            #返回对象
            return cls.obj
        else:
            #直接返回类中制作号的对象
            return cls.obj

    def sayEnglish(self):
        print('呛死你个网吧独子->welcome TO beijing')

#实例化对象
zj1 = Zhongju()
print(zj1)

zj2 = Zhongju()
print(zj2)

zj3 = Zhongju()
print(zj3)

zj4 = Zhongju()
print(zj4)

print('===================================东哥将的单例模式==================================')

class Singleton:
    __instance = None
    __first_init = False
    name = None
    age = None
    def __new__(cls,*args):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self,name,age):
        if not self.__first_init:
            Singleton.name = name
            Singleton.age = age
            self.__first_init = True

s1 = Singleton('老王',16)
print(id(s1))
print(s1.name)

s2 = Singleton('老陈',11)
print(id(s2))
print(s2.name)

s1.age = 111
print(s2.age)