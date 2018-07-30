#### 目录结构
```
.
├── app                    ---  应用目录
│   ├── admin              ---  后台应用
│   │   ├── __init__.py   
│   │   └── views.py
│   ├── home               --- 前台应用
│   │   ├── __init__.py
│   │   └── views.py
│   ├── __init__.py        --- 初始化文件
│   ├── models.py          --- 模型文件
│   ├── static             --- 静态文件目录
│   └── templates          --- 模板目录
├── app.sql         ---  数据文件
├── manage.py       ---  入口文件
├── README.md       ---  项目说明文件
└── req.txt         ---  依赖包文件
```
#### 项目模块
```
admin:
    #会员管理 (列表,权限,)
    #博文管理 (审核(精选,候选),删除,列表,)
    #网站博文分类(添加,列表,修改,删除)
    #评论管理 (列表,删除,屏蔽)


home:
    #会员中心  #登录,注册
    #个人博文  添加,编辑,删除,查看
    #博文评论  添加,查看,删除(个人),编辑(个人)
    #博文标签   (添加新标签,如果已存在,则不在添加)
    #博文分类  (网站分类,个人分类)
    关注,粉丝

    #网站首页
    #网站精选
```
#### 模型
```
Users 会员模型
    id,username,password,email,phone,face,addtime,status

blog  博文模型
    id,title,context,addtime,uid,

type  博文分类
    id, name,pid

tags  博文标签(个人)
    id,tname,uid

comment 评论
    id,bid,uid,con,touid,addtime
    1  2   10  真好,
    2, 2   11  你说的对 10
```