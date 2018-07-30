from flask import Flask,render_template
import itchat
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/addfriends/')
def addfriends():
    for friend in friends:
        print(friend)
    return '添加好友'


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    friends = itchat.get_friends()
    # app.run()
