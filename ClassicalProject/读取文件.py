#读取文件类
'''
打开文件
读取文件
关闭文件
'''
class ReadFile:

    #打开文件
    def __init__(self,path):
        #设定读取的文件路径
        self.filepath = path
        #打开文件(将文件指针存入当前对象)
        self.fp = open(self.filepath,'r')


    #读取文件 (只读取操作)
    def read(self):
        result = self.fp.read()
        print(result)

    #关闭文件
    def __del__(self):
        #自动关闭文件
        self.fp.close()

#实例化对象
rf = ReadFile('/home/conghao/PycharmProjects/python09/01/01.py')
rf.read()

#self的作用贯穿整个对象,所有共用数据存入对象,跨方法使用变量和函数!