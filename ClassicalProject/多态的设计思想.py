#多态：多种状态
#实现
import abc

#规则类（抽象类）
class Animal(metaclass= abc.ABCMeta):
    #叫
    @abc.abstractmethod
    def jiao(self):
        pass

    #尿
    @abc.abstractmethod
    def niao(self):
        pass

    #喝
    @abc.abstractmethod
    def he(self):
        pass


#声明三个类

#狗
class Dog(Animal):
    # 叫
    def jiao(self):
        print('汪汪叫')
    # 尿
    def niao(self):
        print('抬腿尿')
    # 喝
    def he(self):
        print('卷起舌头')

#猫
class Cat(Animal):
    # 叫
    def jiao(self):
        print('喵喵叫')
    # 尿
    def niao(self):
        print('蹲着尿')
    # 喝
    def he(self):
        print('舔着和')

#鸡
class Chick(Animal):
    # 叫
    def jiao(self):
        print('恩~啊 大力点')
    # 尿
    def niao(self):
        print('蹲着尿')
    # 喝
    def he(self):
        print('拿杯子和')

#实例化三个对象
xiaohei = Dog()
xiaohuang = Cat()
xiaohua = Chick()



#行为类
class Action():
    #将传入的动物存入行为对象
    animalobj = None

    def __init__(self,animal):
        self.animalobj = animal

    #叫
    def jiao(self):
        self.animalobj.jiao()
    #尿
    def niao(self):
        self.animalobj.niao()
    #喝
    def he(self):
        self.animalobj.he()

#实例化行为类传入对象
a = Action(xiaohei)

#调用函数
a.jiao()
a.niao()
a.he()

#实例化行为类传入对象
a.animalobj = xiaohua

#调用函数
a.jiao()
a.niao()
a.he()

##实例化行为类传入对象
a.animalobj = xiaohuang

#调用函数
a.jiao()
a.niao()
a.he()