'''
企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？
'''
a1 = 100000 * 0.1
a2 = a1 + 100000 * 0.075
a4 = a2 + 200000 * 0.05
a6 = a4 + 200000 * 0.03
a10 = a6 + 400000 * 0.015
i = int(input('请输入当月利润：'))
if i <= 100000:
    print(i * 0.1)
elif i <= 200000:
    print(a1 + (a - 100000)*0.075)
elif i <= 400000:
    print(a2 + (i - 200000)*0.05)
elif i <= 600000:
    print(a4 + (i - 400000)*0.03)
elif i <= 1000000:
    print(a6 + (i - 600000)*0.015)
else:
    print(a10 + (i - 1000000)*0.01)
