class Ren:

    def __init__(self,name):
        self.name = name
        self.qiang = None
        self.xue = 100

    def shangzidan(self,danjia,zidan):
        danjia.jieshouzidan(zidan)

    def zhuangdanjia(self,qiang,danjia):
        qiang.lianjiedanjia(danjia)

    def naqiang(self,qiang):
        if not self.qiang:
            self.qiang = qiang
        else:
            print('你只能拿一把枪')

    def she(self,diren):
        self.qiang.jifa(diren)

    def diaoxue(self,shashangli):
        if self.xue:
            self.xue -= shashangli
            print(self.name + '的血量为' + str(self.xue))
        else:
            print('敌人已死，恭喜：'+ self.name + '赢得胜利')

class Qiang:
    def __init__(self):
        self.danjia = None

    def lianjiedanjia(self,danjia):
        if not self.danjia:
            self.danjia = danjia
        else:
            print('枪上已经有了弹夹')

    def jifa(self,diren):
        zidan = self.danjia.tanzidan()
        zidan.shanghai(diren)

class ZiDan:
    def __init__(self,shashangli):
        self.shashangli = shashangli
    def shanghai(self,diren):
        diren.diaoxue(self.shashangli)

class DanJia:

    def __init__(self,rongna):
        self.rongna = rongna
        self.rongnaList = []

    def __str__(self):
        return '弹夹内此时的子弹数量为' + str(len(self.rongnaList)) + '/' + str(self.rongna)

    def jieshouzidan(self,zidan):
        if len(self.rongnaList) < self.rongna:
            self.rongnaList.append(zidan)
        else:
            print('弹夹满了')

    def tanzidan(self):
        if self.rongnaList:
            zidan = self.rongnaList.pop()
            return zidan
        else:
            print('弹夹已将空了')

laowang = Ren('老王')


danjia = DanJia(20)
print(danjia)
i = 0
while i < 20:
    zidan = ZiDan(5)
    laowang.shangzidan(danjia,zidan)
    i += 1
print(danjia)

qiang = Qiang()
laowang.zhuangdanjia(qiang,danjia)

diren = Ren('敌人')
laowang.naqiang(qiang)

while True:
    j = int(input('要开几枪：'))
    i = 0
    while i < j:
        laowang.she(diren)
        i += 1
    if not danjia.rongnaList:
        break