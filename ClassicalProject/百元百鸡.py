#100元买100只鸡，3元公鸡，1元母鸡，0.5元鸡蛋，能有多少种组合
#x = 100 - z - y
'''
import time
x = 0 #公鸡个数
y = 1 #母鸡个数
z = 0 #小鸡个数
sun = 0
while y < 100:
    z = (200 - 2 * y) / 2.5
    p = int(z)
    if z == p:
        sun += 1
        print('公鸡数：%d + 母鸡数：%d + 鸡蛋数：%d = 100'%(100-z-y,y,z))
        time.sleep(0.3)
    y += 1
print('有%d种排列'%sun)
'''




num = 0
y = 0
while y <= 100:
    x = 0
    while x < 34:
        z = 0
        while z <= 100:
            if (x + y + z == 100) and ((3*x + y + 0.5*z) == 100):
                num += 1
                print(x,y,z)
            z += 1
        x += 1
    y += 1
print(num)


