from flask import Flask

# 使用模块下面的Flask函数创建一个app对象
app = Flask(__name__)

# 启动调试模式：方法一
# app.debug = True
# 启动调试模式：方法二：app.run(debug=True)
# 启动调试模式之后，每次改变应用内容，都会自动刷新，而不用手动点击刷新


# 绑定路由和视图函数方法一：使用装饰器
@app.route('/')
def hello_word():
    return 'hello word!'
# 绑定路由和视图方法二：
# app.add_url_rule('/',view_func=hello_word)

# 路由携带参数：可以强制携带int 和 float
@app.route('/admin/<username>/<int:age>/<float:money>')
def admin(username,age,money):
    return 'admin' + '/username:'+username+'/age:'+str(age)+str(money)


# 只在本脚本运行时执行
if __name__ == '__main__':
    # 启动flask服务，并且设置ip和端口(0.0.0.0代表所有本机的ip都开放，即127.0.0.1和10.11.216.xxx等只要是本机的都开放，默认端口就是5000)
    app.run(debug=True,host='0.0.0.0',port=5000)


'''
本练习知识点：
1、绑定路由和视图函数的两种方法
2、路由携带参数（类似于子组）的方法，及数据类型
3、debug(两种) host（0.0.0.0） port
'''