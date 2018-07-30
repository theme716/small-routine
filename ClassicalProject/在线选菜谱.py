# 菜谱在线选择系统
def caipu():
    x = int(input("请输入您要选择的套餐，回复相应的数字进行查看\n"
                  "0----》退出\n"
                  "1----》套餐一\n"
                  "2----》套餐二\n"
                  "3----》套餐三\n"))
    if x == 1:
        print("红烧茄子+米饭\n")
    elif x == 2:
        print("鱼香肉丝+馒头\n")
    elif x == 3:
        print("包子豆浆")
    else:
        print("退出成功")


caipu()

# 学生登录成绩查询系统
student = {("damin", "admin"), ("sun", "123")}


def student1():
    x = input("请输入用户名\n")
    y = input("请输入密码\n")
    while (x, y) in student:
        print("登录成功，请查看成绩\n")
        cat()

    else:
        print("登录失败\n")


def cat():  # 成绩查询函数
    a = input("请输入您要查看成绩的学生证号\n")  # 用户登录成功后输入学生证号进行查询
    list1 = {"110", "120"}
    dict1 = {"110": "语文：54\n数学：67\n英语：88\n", "120": "语文：66\n数学：98\n英语：88\n"}  # 建立字典，通过目录索引进行查询
    while a in list1:
        print("正在查询")
        b = dict1[a]  # 取值查询
        print(b)
        break
    else:  # 学生不存在直接输出
        print("您查询的学生不存在")
        s = "请核对后查询"
        return s


student1()