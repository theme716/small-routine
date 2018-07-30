import itchat
def weixinlogin():
    itchat.auto_login(hotReload=True)
    friends = itchat.get_friends()
    for friend in friends:
        print(friend)

weixinlogin()