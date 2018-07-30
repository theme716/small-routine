'''
# 版本一：复用性差，没有return,其他使用者不能得到返回值
def fab(max):
    n,a,b = 1,5,7
    while n < max:
        print(b)
        a,b = b,a+b
        n += 1

if __name__ == '__main__':
    fab(10) # 1 1 2 3 5 8 13 21 34 55


#版本二：该函数在运行中占用的内存会随着参数 max 的增大而增大，如果要控制内存占用，最好不要用 List
def fab(max):
    n,a,b = 0,0,1
    L = []
    while n < max:
        L.append(b)
        a,b = b,a+b
        n += 1
    return L
'''
#版本三：通过iterable对象来迭代(缺点是，没有第一版的代码简介)
'''
class Fab:
    def __init__(self,max):
        self.max = max
        self.n,self.a,self.b = 0,0,1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a,self.b = self.b,self.a+self.b
            self.n += 1
            return r
        raise StopIteration()  #停止执行迭代

if __name__ == '__main__':
    fab = Fab(10)
    for i in fab:
        print(i)
'''

#版本四：
'''
def fab(max):
    n,a,b = 0,0,1
    while n < max:
        # print(b)
        yield b  #存在yield而没有return,就会成为一个生成器
        a,b = b,a+b
        n += 1

if __name__ == '__main__':
    a = fab(10)
    for i in a:
        print(i)
# yield的作用：
#     把一个函数变成一个generator,带有yield的函数不再是一个普通的函数，
#     python解释器会将其视为一个generator，调用该函数的时候不会执行，
#     而是返回一个iterable对象！for 循环该对象的时候，遇到yield会返回一个迭代值，
#     然后停止执行，下一次从yield下一条语句开始执行。
'''


# 判断一个函数是否是生成器（generator函数）
# 使用isgeneratorfuncition判断
'''
from inspect import isgeneratorfunction
def fab(max):
    n,a,b = 0,0,1
    while n < max:
        # print(b)
        yield b  #存在yield而没有return,就会成为一个生成器
        a,b = b,a+b
        n += 1
if __name__ == '__main__':
    print(isgeneratorfunction(fab)) #True
    print(isgeneratorfunction(range)) #False
'''

# 使用types模块判断类别
'''
import types
def fab(max):
    n,a,b = 0,0,1
    while n < max:
        # print(b)
        yield b  #存在yield而没有return,就会成为一个生成器
        a,b = b,a+b
        n += 1
f = fab(5)
print(isinstance(range,types.GeneratorType)) # False
print(isinstance(range(5),types.GeneratorType)) # False
print(isinstance(fab,types.GeneratorType)) # False
print(isinstance(f,types.GeneratorType)) # True
print(isinstance(fab,types.FunctionType)) # True
print(isinstance(max,types.BuiltinFunctionType)) # True
'''

