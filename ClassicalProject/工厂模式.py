# 工厂模式

print('=========================这是简单工厂模式=============================')
'''
class BaoMa:
    def move(self):
        print('宝马在移动')
    def stop(self):
        print('宝马停车')

class BenChi:
    def move(self):
        print('奔驰在移动')
    def stop(self):
        print('奔驰在移动')


class CarFactory:
    def createCar(self,typeName):
        if typeName == '宝马':
            self.car = BaoMa()
        elif typeName == '奔驰':
            self.car = BenChi()
        return self.car

class CarStory:
    def order(self,typeName):
        self.car = CarFactory().createCar(typeName)
        self.car.move()

car = CarStory()
car.order('奔驰')
'''

'''
class AppleCake:
    def __init__(self):
        self.taste = '苹果味道'

class OrangeCake:
    def __init__(self):
        self.taste = '橘子味道'

class CakeFactory:
    def creatCake(self,weidao):
        if weidao == '橘子':
            self.cake = OrangeCake()
        elif weidao == '苹果':
            self.cake = AppleCake()
        return self.cake

class CakeStory:
    def __init__(self):
        self.factory = CakeFactory()
    def taste(self,weidao):
        cake = self.factory.creatCake(weidao)
        print(cake.taste,'的蛋糕')

a = CakeStory()
a.taste('橘子')
'''
print('============================这才是真正的工厂模式=============================')


class BaoMa:
    def move(self):
        print('宝马在移动')

    def stop(self):
        print('宝马停车')


class BenChi:
    def move(self):
        print('奔驰在移动')

    def stop(self):
        print('奔驰在移动')


class CarFactory:
    def createCar(self, typeName):
        if typeName == '宝马':
            self.car = BaoMa()
        elif typeName == '奔驰':
            self.car = BenChi()
        return self.car


class CarStory:
    def createCar(self, typeName):
        pass

    def order(self, typeName):
        self.car = self.createCar(typeName)
        self.car.move()


class HaoHuaCarStory(CarStory):
    def createCar(self, typeName):
        self.car = CarFactory().createCar(typeName)
        return self.car


haohuacarstory = HaoHuaCarStory()
haohuacarstory.order('宝马')
