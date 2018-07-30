from flask import Flask,request,make_response,session
import os

app = Flask(__name__)
app.secret_key = os.urandom(20)


# 如何读取cookie
@app.route('/')
def index():
    # 获取一条cookie
    username = request.cookies.get('username',None)
    print(username)
    if username:
        return username
    else:
        return '未登录'



# 如何设置cookie
# @app.route('/login/')
# def login():
#     response = make_response('ok')
#     response.set_cookie('username','小丽')
#     return response


# 读取session
@app.route('/news/')
def news():
    print(session)
    if 'username' in session:
        return session['username']
    else:
        return '未登陆'

# 设置session
@app.route('/login/<username>')
def login(username):
    session['username'] = username
    print(session)
    return '登陆成功'

if __name__ == '__main__':
    app.run(debug=True)