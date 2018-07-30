#模式一

i = 1
while i <= 9:
    k = 1
    while k <= (i - 1):
        print('-'*12,end='')
        k += 1

    j = 1
    while j <= (10 - i):
        print('%d * %d = %-4d'%((11 - i - j),(10 - i),(11 - i - j)*(10 - i)),end='')
        j += 1
    print('')
    i += 1


#模式二
print('')
i = 1
while i <= 9:
    k = 1
    while k <= (i - 1) :
        print('-'*12,end='')
        k += 1
    j = 9
    while j >= i:
        print('%d * %d = %-4d'%((j-i+1),(10-i),(j-i+1)*(10-i)),end='')
        j -= 1
    print('')
    i += 1


#模式三
print()
H = 9
while H >= 1:
    k = 0  # 空的数量
    while k < (9 - H):
        print(' ' * 12, end='')
        k += 1

    L = 1
    while L <= H:
        print('%d * %d = %-4d'%((H + 1 - L),H,(H + 1 - L)*H),end='')
        L += 1
    print('')
    H -= 1


#模式四
print('')

i = 9
while i >= 1:
    k = 9
    while k  > i:
        print('-' * 12, end='')
        k -= 1

    j = 9
    while (10-j) <= i:
        print('%d * %d = %-4d'%((j-9+i),i,(j-9+i)*i),end='')
        j -= 1
    print('')
    i -= 1



#模式一
print()
L = 9
while L >= 1:

    K = 1#控制空的数量
    while K <= (L - 1):
        print(' '*12, end='')
        K += 1

    H = 1#控制输出
    while H <= (10-L):
        print('%d * %d = %-4d'%((11-L-H),(10 - L),(11-L-H) * (10 - L)),end='')
        H += 1

    print('')#换行
    L -= 1

print('')
#模式二


