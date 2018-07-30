import tkinter

root = tkinter.Tk()
root.minsize(350,530)


btn1 = tkinter.Button(root,text = '菜单',bg = '#DCDCDC')
btn1.place(x = 0,y = 0,width = 50,height =30)
btn1 = tkinter.Button(root,bg = '#DCDCDC')
btn1.place(x = 50,y = 0,width = 300,height =30)

#显示标签
show = tkinter.Label(root,text = '0',bg = '#DCDCDC',font = ('微软雅黑',20),anchor = 'se')
show.place(x = 0,y = 30,width = 350,height =90)

btn1 = tkinter.Button(root,text = 'MC',bg = '#DCDCDC',font = ('微软雅黑',7))
btn1.place(x = 0,y = 120,width = 58.3,height =30)
btn1 = tkinter.Button(root,text = 'MR',bg = '#DCDCDC',font = ('微软雅黑',7))
btn1.place(x = 58.3,y = 120,width = 58.3,height =30)
btn1 = tkinter.Button(root,text = 'M+',bg = '#DCDCDC',font = ('微软雅黑',7))
btn1.place(x = 116.6,y = 120,width = 58.3,height =30)
btn1 = tkinter.Button(root,text = 'M-',bg = '#DCDCDC',font = ('微软雅黑',7))
btn1.place(x = 174.9,y = 120,width = 58.3,height =30)
btn1 = tkinter.Button(root,text = 'MS',bg = '#DCDCDC',font = ('微软雅黑',7))
btn1.place(x = 233.2,y = 120,width = 58.3,height =30)
btn1 = tkinter.Button(root,text = 'M',bg = '#DCDCDC',font = ('微软雅黑',7))
btn1.place(x = 291.5,y = 120,width = 58.3,height =30)

btn1 = tkinter.Button(root,text = '%',bg = '#DCDCDC')
btn1.place(x = 0,y = 150,width = 87.5,height =55)
btn1 = tkinter.Button(root,text = '√',bg = '#DCDCDC')
btn1.place(x = 87.5,y = 150,width = 87.5,height =55)
btn1 = tkinter.Button(root,text = 'X*2',bg = '#DCDCDC')
btn1.place(x = 175,y = 150,width = 87.5,height =55)
btn1 = tkinter.Button(root,text = '1/x',bg = '#DCDCDC')
btn1.place(x = 262.5,y = 150,width = 87.5,height =55)

btn1 = tkinter.Button(root,text = 'CE',bg = '#DCDCDC')
btn1.place(x = 0,y = 205,width = 87.5,height =55)
btn1 = tkinter.Button(root,text = 'C',bg = '#DCDCDC')
btn1.place(x = 87.5,y = 205,width = 87.5,height =55)
btn1 = tkinter.Button(root,text = 'DEL',bg = '#DCDCDC')
btn1.place(x = 175,y = 205,width = 87.5,height =55)
btn1 = tkinter.Button(root,text = '/',bg = '#DCDCDC')
btn1.place(x = 262.5,y = 205,width = 87.5,height =55)

btn1 = tkinter.Button(root,text = '7',bg = '#F5F5F5',font = ('微软雅黑',14))
btn1.place(x = 0,y = 260,width = 87.5,height =55)
btn1 = tkinter.Button(root,text = '8',bg = '#F5F5F5',font = ('微软雅黑',14))
btn1.place(x = 87.5,y = 260,width = 87.5,height =55)
btn1 = tkinter.Button(root,text = '9',bg = '#F5F5F5',font = ('微软雅黑',14))
btn1.place(x = 175,y = 260,width = 87.5,height =55)
btn1 = tkinter.Button(root,text = '*',bg = '#DCDCDC')
btn1.place(x = 262.5,y = 260,width = 87.5,height =55)

btn1 = tkinter.Button(root,text = '4',bg = '#F5F5F5',font = ('微软雅黑',14))
btn1.place(x = 0,y = 315,width = 87.5,height =55)
btn5 = tkinter.Button(root,text = '5',bg = '#F5F5F5',font = ('微软雅黑',14))
btn5.place(x = 87.5,y = 315,width = 87.5,height =55)
btn1 = tkinter.Button(root,text = '6',bg = '#F5F5F5',font = ('微软雅黑',14))
btn1.place(x = 175,y = 315,width = 87.5,height =55)
btn1 = tkinter.Button(root,text = '-',bg = '#DCDCDC')
btn1.place(x = 262.5,y = 315,width = 87.5,height =55)

btn1 = tkinter.Button(root,text = '1',bg = '#F5F5F5',font = ('微软雅黑',14))
btn1.place(x = 0,y = 370,width = 87.5,height =55)
btn1 = tkinter.Button(root,text = '2',bg = '#F5F5F5',font = ('微软雅黑',14))
btn1.place(x = 87.5,y = 370,width = 87.5,height =55)
btn1 = tkinter.Button(root,text = '3',bg = '#F5F5F5',font = ('微软雅黑',14))
btn1.place(x = 175,y = 370,width = 87.5,height =55)
btn1 = tkinter.Button(root,text = '+',bg = '#DCDCDC')
btn1.place(x = 262.5,y = 370,width = 87.5,height =55)

btn1 = tkinter.Button(root,text = '+-',bg = '#DCDCDC')
btn1.place(x = 0,y = 425,width = 87.5,height =55)
btn1 = tkinter.Button(root,text = '0',bg = '#F5F5F5',font = ('微软雅黑',14))
btn1.place(x = 87.5,y = 425,width = 87.5,height =55)
btn1 = tkinter.Button(root,text = '.',bg = '#DCDCDC')
btn1.place(x = 175,y = 425,width = 87.5,height =55)
btn1 = tkinter.Button(root,text = '=',bg = '#DCDCDC')
btn1.place(x = 262.5,y = 425,width = 87.5,height =55)
btn1 = tkinter.Button(root,text = 'ck出品',bg = '#DCDCDC')
btn1.place(x = 0,y = 480,width = 350,height =55)

listVar = []
flage = False
flage2 = False
#数字按键的显示
def numVar(t):
    global flage
    global flage2
    if '.' not in show['text']:
        if flage == True:
            show['text'] = '0'
            flage = False
            flage2 = False
        show['text'] += t
        if show['text'][0] == '0':
            show['text'] = show['text'][1:]
    elif show['text'].count('.') == 1:
        if t != '.':
            if flage == True:
                show['text'] = '0'
                flage = False
                flage2 = False
            show['text'] += t
            if show['text'][0] == '0':
                show['text'] = show['text'][1:]
#运算按键的显示
def ouVar(t):
    global flage
    listVar.append(show['text'])
    listVar.append(t)
    flage = True
#计算
def jisuan(t):
    a = ''.join(listVar[:-1])
    show['text'] = str(eval(a))
    listVar.clear()
    listVar.append(show['text'])#将结果放入列表中
    listVar.append(t)#为列表添加运算符
def main(e):
    t = e.widget['text']
    global show
    global flage
    global flage2
    if t in '1234567890.':
        numVar(t)
    elif e.widget['text'] in '+-*/':
        if not flage2:
            ouVar(t)
            if len(listVar) > 3:
                jisuan(t)
                flage2 = True
    elif e.widget['text'] == '=':
        listVar.append(show['text'])#先将屏幕上最后一次输入的数字放到列表中
        show['text'] = str(eval( ''.join(listVar)))#列表中计算并显示到屏幕上
        listVar.clear()#清空列表
        flage = True
btn5.bind_class('Button','<Button-1>',main)


root.mainloop()
