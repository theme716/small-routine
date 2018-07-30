from flask import Flask,abort,render_template,request
'''
本测试知识点：
1、抛出异常，
2、抛出自己定义的404等页面
3、接受get post请求
4、request方法 
'''
app = Flask(__name__)
app.debug = True

# 1/111111111111111111
# 抛出异常测试：

# abort 定义某个路由要抛出错误
@app.route('/one/')
def one():
    # 抛出错误，如果在template有404.html，那么会直接抛出这个页面
    abort(404)
    # abort(500)


# 定植错误页面
# 装饰器的404是高数flask，这是遇到404错误时候抛出的页面
# return 最后的404是高数浏览器，这是一个404错误，显示在F12的network里面的请求的状态就是404，如果没有这个，会显示200
@app.errorhandler(404)
def two(error):
    print('=====')
    print(error) #404 Not Found: The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.
    print('======')
    return render_template('404.html'),404

#2/222222222222222222222222222222
# 接受post 请求
@app.route('/three/',methods=['GET','POST'])
def three():
    if request.method == 'POST':
        return 'post'
    elif request.method == 'GET':
        return render_template('for_three.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000')