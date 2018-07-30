import os

name = input('你要判断的文件的绝对路径是什么:')
def fileSize(filename):
	fileList = os.listdir(filename)
	totalSize = 0
	for name in fileList:
		fileAbs = os.path.join(filename,name)
		if os.path.isfile(fileAbs):
			totalSize += os.path.getsize(fileAbs)	
		elif os.path.islink(fileAbs):
			totalSize += os.path.getsize(fileAbs)
		elif os.path.isdir(fileAbs):
			totalSize +=fileSize(fileAbs)
	return totalSize


size = fileSize(name)
print(size)

