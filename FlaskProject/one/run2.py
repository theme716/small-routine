from flask import Flask,redirect,url_for

app = Flask(__name__)
app.debug=True


# 重定向练习一：使用redirect重定向，使用url_for解析路由，url_for函数的参数是另一个视图函数的函数名
@app.route('/aaaaaaa/')
def hello_word():
    return 'hello_word'
@app.route('/six/<username>')
def two(username):
    print(url_for('hello_word',username=username)) # 打印出来 /aaaaaaa/?username=aaaa
    return redirect(url_for('hello_word'))


# 重定向练习三：结合参数
@app.route('/ccc/<username>')
def ccc(username):
    return username
@app.route('/cat/<check>')
def cat(check):
    print(url_for('ccc',username=check)) #/ccc/thisiscat
    return redirect(url_for('ccc',username=check)) #这样子实现了给重定向的路由传参,最终，传入check的参数，经过重定向传参，传到了要定向的那里

# 重定向练习二：
@app.route('/bbb/<username>')
def bbb(username):
    return username
with app.test_request_context():
    print(url_for('bbb',username='ckttty')) #/bbb/ckttty


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8081')


'''
重定向总结：
1、url_for('bbb',username='ckttty')这样带有参数的重定向
    如果bbb函数的路由里面有<username>接受参数，那么ckttty将作为路由参数参数传递过去，即/url/url参数 的格式
    如果bbb函数的路由里面没有<username>接受参数，那么ckttty将成为get传参数，即/url/?username=参数 的格式
    具体比较参照上面试验2和实验三
2、redirect 重定向，url_for解析路由，url_for里面可以有其他实参作为参数
    redirect 和 url_for都需要引入这连个函数
'''

