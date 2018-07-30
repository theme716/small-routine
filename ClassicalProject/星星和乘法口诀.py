"""
# 菱形小星星
    *
   ***
  *****
 *******
*********



(1) 对于任意个星星   总行数是多少 总行数 = n // 2 +1
(2) 对于任意行数  那么当前行数是多少个星星  2*当前行 -1
(3) 对于任意行数  当前行数是多少个空格呢  当前的行的空格 =  总行数 - 当前行
1=>4
2=>3
3=>2
4=>1
"""



def ceshi100(n):
	zonghangshu = n // 2 + 1
	i = 1
	while i<= zonghangshu:
	
		k = zonghangshu - i
		while k > 0:
			print(' ',end='')
			k-=1

		j = 1
		while j<=2*i -1:
			print("*",end='')
			j+=1
		print()
		i+=1
ceshi100(13)

def ceshi1001(n):
	zonghangshu = n // 2 + 1
	i = zonghangshu
	while i>=0:
	
		k = zonghangshu - i
		while k > 0:
			print(' ',end='')
			k-=1

		j = 1
		while j<=2*i -1:
			print("*",end='')
			j+=1
		print()
		i -= 1

ceshi1001(13)

'''
print("<=================================>")
# res = "*" * 10
# print(res,end='')
def ceshi1002(n):
	zonghangshu = n // 2 + 1
	i = zonghangshu
	while i>=0:
		print(' '*(zonghangshu - i),end='')
		print("*"*(2*i -1),end='')
		print()
		i-=1

ceshi1002(13)
'''
res1 = [1,2,3]
res2 = [4,5,6]
print(res1+res2)

#99 乘法表
i= 1
while i<=9:
	k=9-i
	while k>0:
		print('       ',end='')
		k-=1

	j = 1
	while j<=i:
		print("%d*%d=%2d "%(i,j,i*j),end='')
		j+=1
	print()
	i+=1


print()
print("---999888---")
def ceshi900():
	str = ''
	i= 9
	while i>0:
		k=9-i
		while k>0:
			# print('       ',end='')
			str += '       '
			k-=1

		j = 1
		while j<=i:
			# print("%d*%d=%2d "%(i,j,i*j),end='')
			str += "%d*%d=%2d "%(i,j,i*j)
			j+=1
		str += '\n'
		i-=1
	return str

res = ceshi900()
print(res)




i = 1
j = 1
while i <= 9:
    if i <= 5:
        k = 1
        while k <= (5-i):
            print(' '*2,end='')
            k += 1
        j = 1
        while j <= (i - 1)*2+1:
            print('★',end='')
            j += 1
        print('')
    else:
        k = 1
        while k <= (i - 5):
            print(' ' * 2, end='')
            k += 1
        j = 1
        while j <= (9-i)*2+1:
            print('★', end='')
            j += 1
        print('')
    i += 1

#方法二输出三角形

# i = '*'
# for x in range(1,10,2):
#     print((i*x).center(9))




















