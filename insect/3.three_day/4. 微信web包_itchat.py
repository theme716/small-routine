import itchat
import random,time

mes_list = ['一个忠告：找对象一定要找个空调度数合得来的。','你觉得你充满睿智，每次在群里面叱咤风云，点评天下，好不威风。其实你知道，你就是个杠精而已。','别人：拍照，上传。你：拍照、拍照、拍照、拍照、拍照、拍照、拍照、拍照、拍照、拍照、拍照、拍照、拍照。。。一键删除。']

# 登录
# 设置了hotReload = True,下次登录只想要手机端点击确认
itchat.auto_login(hotReload=True)

# 获取全部的好友
# friends = itchat.get_friends()

# 朋友信息
# for friend in friends:
#     print(friend)
#     print('==================')
    # UserName:唯一的id
    # NickName:昵称
    # RemarkName：备注称呼
    # Signature:个性签名

# 发送消息
# for friend in friends:
#     if friend['NickName']=='cktttty':
#         itchat.send('炸了',toUserName=friend['UserName'])

# 获取自己的信息,并且给自己发消息
my = itchat.get_friends()[0]
myusername = my['UserName']
# itchat.send('ok',myusername)

@itchat.msg_register('Text')  #Text表示接受文字消息
def text_reply(msg): #msg 接收到的消息
    '''
    :param msg: 接受到的消息列表
    :return: 回复的消息
    '''
    if msg['FromUserName'] == '@5d62c3cb356b505e40b884eee30226bd2139b067084afe3ea0943df129af2e84':
        return msg['Text']
    # for s,y in msg.items():
    #     print(s,'====',y)
        '''
        MsgId ==== 1175141688288204467
        FromUserName ==== @5d62c3cb356b505e40b884eee30226bd2139b067084afe3ea0943df129af2e84
        ToUserName ==== @1a80eb06a9ad2723e6aff4966c977d7eded04232ac3fbc75d0a5a10d296acece
        MsgType ==== 1
        Content ==== 喂
        Status ==== 3
        ImgStatus ==== 1
        CreateTime ==== 1528829131
        VoiceLength ==== 0
        PlayLength ==== 0
        FileName ====
        FileSize ====
        MediaId ====
        Url ====
        AppMsgType ==== 0
        StatusNotifyCode ==== 0
        StatusNotifyUserName ====
        RecommendInfo ==== {'UserName': '', 'NickName': '', 'QQNum': 0, 'Province': '', 'City': '', 'Content': '', 'Signature': '', 'Alias': '', 'Scene': 0, 'VerifyFlag': 0, 'AttrStatus': 0, 'Sex': 0, 'Ticket': '', 'OpCode': 0}
        ForwardFlag ==== 0
        AppInfo ==== {'AppID': '', 'Type': 0}
        HasProductId ==== 0
        Ticket ====
        ImgHeight ==== 0
        ImgWidth ==== 0
        SubMsgType ==== 0
        NewMsgId ==== 1175141688288204467
        OriContent ====
        EncryFileName ====
        User ==== {'MemberList': <ContactList: []>, 'Uin': 0, 'UserName': '@5d62c3cb356b505e40b884eee30226bd2139b067084afe3ea0943df129af2e84', 'NickName': 'cktttty', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=676164623&username=@5d62c3cb356b505e40b884eee30226bd2139b067084afe3ea0943df129af2e84&skey=@crypt_b70527dd_1cdf94914120918a7c4de515eddc4992', 'ContactFlag': 3, 'MemberCount': 0, 'RemarkName': 'cktttty', 'HideInputBarFlag': 0, 'Sex': 0, 'Signature': '', 'VerifyFlag': 0, 'OwnerUin': 0, 'PYInitial': 'CKTTTTY', 'PYQuanPin': 'cktttty', 'RemarkPYInitial': 'CKTTTTY', 'RemarkPYQuanPin': 'cktttty', 'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 0, 'AttrStatus': 4133, 'Province': '', 'City': '', 'Alias': '', 'SnsFlag': 0, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': '', 'EncryChatRoomId': '', 'IsOwner': 0}
        Type ==== Text
        Text ==== 喂
        '''
itchat.run()


# 登出
# itchat.logout()
