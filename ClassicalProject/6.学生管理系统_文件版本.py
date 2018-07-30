stuInfos = []
def printMenu():
	#输出打印菜单函数定义
	print('*' * 30)
	print('     学生管理系统 v6.6')
	print('1. 添加学生信息')
	print('2. 删除学生信息')
	print('3. 修改学生信息')
	print('4. 查询学生信息')
	print('5. 显示所有学生信息')
	print('0. 退出系统')
	print('*' * 30)
def inputstuInfos():
	#提示并获取学生的信息,添加函数定义
	newName = input('请输入新同学的姓名：')
	newSex = input('请输入新同学的性别：')
	newPhone = input('请输入新同学的联系方式：')
	dictvar = {}
	dictvar['name'] = newName
	dictvar['sex'] = newSex
	dictvar['phone'] = newPhone
	# 将字典添加进列表
	stuInfos.append(dictvar)
def alter():
	# 修改学生的信息
	# 3.1 要修改的学号
	stuId = int(input('请输入要修改的学生的学号:'))

	# 3.2 该学生的新信息
	newName = input('请输入新同学的姓名：')
	newSex = input('请输入新同学的性别：')
	newPhone = input('请输入新同学的联系方式：')

	stuInfos[stuId]['name'] = newName
	stuInfos[stuId]['sex'] = newSex
	stuInfos[stuId]['phone'] = newPhone
def fine():
	# 查找学生信息函数定义
	# 输入要查找的学生的学号
	stuId = int(input('请输入要查找的学生的学号:'))

	# 打印学生信息
	print('%s同学的性别为:%s,联系方式为%s' % (stuInfos[stuId]['name'], stuInfos[stuId]['sex'], stuInfos[stuId]['phone']))
def output():
	# 输出所有学生信息函数
	print('*' * 30)
	print('学生的信息如下')
	print('学生序号  学生姓名  学生性别 联系方式')
	for x, i in enumerate(stuInfos):
		if len(i) == 0:
			pass
		else:
			print(x, '\t ', '%s 	%s 	%s' % (i['name'], i['sex'], i['phone']))
	print('*' * 30)
def main():
	while True:
		#1.打印功能提示
		printMenu()
		#2.获取功能的选择
		key = input('请输入功能对应的数字:')
		#3.根据用户的选择，进行相应的操作
		if key == "1":
			#添加学生信息
			inputstuInfos()
		elif key == '2':
			#提示要输出的学生序号
			stuId =int(input('请输入要修改的学生的学号:'))
			#清空字典
			stuInfos[stuId].clear()
		elif key == '3':
			alter()
		elif key == '4':
			fine()
		elif key == '5':
			output()
		elif key == '0':
			break


main()
print('欢迎使用本系统')


#减少函数打磨 提高函数的使用率
#5的输出所有的时候按照年龄排序，按照姓名排序