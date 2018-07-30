import os 

'''
#获取目录列表
nameList = os.listdir('./AAA/')
print(nameList)

#重命名
for x in nameList:
	os.rename('./AAA/'+x,'./AAA/'+'[ck出品]'+x)
'''

#第二个版本

#提示并获取要重命名的文件夹
needRename = input('请输入要批量重命名的文件夹:')

#获取目录列表
nameList = os.listdir('./'+needRename)

#重命名
for x in nameList:
	os.rename('./'+needRename+'/'+x,'./'+needRename+'/'+'[ck出品]'+x)




