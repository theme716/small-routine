import tkinter
import tkinter.filedialog
import zipfile
import os
import tkinter.messagebox

class ObjZip:
    #创建窗口
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.minsize(380,300)
        self.zipButton()
        self.bindButton()
        self.root.mainloop()
    def zipButton(self):
        self.btn1 = tkinter.Button(self.root, text='选择文件')
        self.btn1.place(x=20, y=0, width=100, height=80)
        self.btn2 = tkinter.Button(self.root, text='压缩')
        self.btn2.place(x=140, y=0, width=100, height=80)
        self.btn3 = tkinter.Button(self.root, text='解压')
        self.btn3.place(x=260, y=0, width=100, height=80)
        self.show = tkinter.Label(self.root, text='文件信息：', bg='#DCDCDC', anchor='nw')
        self.show.place(x=20, y=100, width=340, height=180)
    #要压缩的文件方法
    def openFile(self,e):
        self.filepath = tkinter.filedialog.askopenfilenames(title = '要压缩哪些文件')
        self.show['text'] = '\n'.join(self.filepath)
    #压缩方法
    def saveFile(self,e):
        dirPath = tkinter.filedialog.asksaveasfilename(title = '压缩到哪个文件夹')
        zp = zipfile.ZipFile(dirPath + '.zip','w')
        for p in self.filepath:
            zp.write(p,os.path.basename(p))
        zp.close()
        tkinter.messagebox.showinfo(title = '提示',message='压缩成功')
    #解压方法
    def jieZip(self,e):
        filePath = tkinter.filedialog.askopenfilename(title = '请选择解压缩的文件',filetypes = (('zip压缩文件','*.zip'),))
        zp = zipfile.ZipFile(filePath,'r')
        filePath2 = tkinter.filedialog.asksaveasfilename(title = '解压到哪里')
        zp.extractall(filePath2)
        zp.close()
        tkinter.messagebox.showinfo(title = '提示',message='解压成功')
    #绑定事件
    def bindButton(self):
        self.btn1.bind('<ButtonRelease-1>',self.openFile)
        self.btn2.bind('<ButtonRelease-1>',self.saveFile)
        self.btn3.bind('<ButtonRelease-1>',self.jieZip)

oz = ObjZip()
#改进：压缩文件夹
#选择压缩模式
#选择全部或者解压部分