import random
romes = [[],[],[]]
teacher = ['A','B','C','D','E','F','G','H']

for name in teacher:
    i = random.randint(0,2)
    romes[i].append(name)

#打印 每个办公室里面都有谁
'''
room1 = romes[0]
print('第一个办公室里面有：%s'%room1)
room2 = romes[1]
print('第一个办公室里面有：%s'%room2)
room3 = romes[2]
print('第一个办公室里面有：%s'%room3)
'''

'''
for room1 in romes[0]:
    print(room1,end='')
print('')
print('*'*20)

for room1 in romes[1]:
    print(room1, end='')
print('')
print('*'*20)

for room1 in romes[2]:
    print(room1, end='')
print('')
print('*'*20)

'''

for room in romes:
        for x in room:
            print(x,end='')
        print('')
        print('*'*30)



