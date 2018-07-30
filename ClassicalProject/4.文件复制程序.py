#提示并获取要复制的文件名
name = input('要复制的文件名')

#打开要复制的文件
f = open(name,'r')

#创建一个新文件,用来存储源文件的数据内容
findPosition = name.find('.')

newName = name[:findPosition] + '[附件]' + name[findPosition
:] 

p = open(newName,'w')

#复制
#第一种(很危险,容易挤爆内存)
#content = f.read()
#p.write(content)

#第二种(可以一行一行复制过去,减少内存压力)
#for lineContent in f.readlines():
#	p.write(lineContent)

#第三种(安全选择)
while True:

	lineContent = f.readline()
	if len(lineContent) > 0:
		p.write(lineContent)
	else:
		break

#关闭文件
f.close()
p.close()








