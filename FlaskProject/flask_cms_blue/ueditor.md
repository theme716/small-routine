

1,项目目录结构

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

2,使用蓝图构建项目模块



3,项目模块:

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


4,模型

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




密码加密
    import hashlib
    # 创建md5对象
    hl = hashlib.md5()
    # 执行md5加密
    hl.update(pwd.encode(encoding='utf-8'))
    # 获取加密后的密文
    return hl.hexdigest()

session
    # 密钥
    app.secret_key = 'abcdef'





百度富文本编辑器的使用

下载地址:http://ueditor.baidu.com/website/download.html

[1.4.3.3 PHP 版本] UTF-8版 


1,文件解压.放置在 static目录下
    yc@yc-virtual-machine:~/py08/25-flask/app/static$ ls
    public  ueditor  uploads

    static/ueditor/

2,使用编辑器

    <!-- 配置文件 -->
    <script type="text/javascript" src="/static/ueditor/ueditor.config.js"></script>
    <!-- 编辑器源码文件 -->
    <script type="text/javascript" src="/static/ueditor/ueditor.all.js"></script>

    <!-- 加载编辑器的容器 -->
    <script id="container" name="content" type="text/plain">
        这里写你的初始化内容
    </script>
    
    <!-- 实例化编辑器 -->
    <script type="text/javascript">
        var ue = UE.getEditor('container',{
          serverUrl:'/ueditconfig/'
        });
    </script>

    注意在实例化编辑器的时候,指定serverUrl地址去解析配置文件

3,定义配置文件读取的 视图函数

    3,在static/目录下创建 uploads/目录,给上传的文件使用


    1,app/__init__.py文件中去定义BASE_DIR,需要导入 os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


    2,app/home/views.py 文件中定义路由和视图函数
    需要导入 os,json,time,random,re



        # ueditor读取配置文件
        @home.route('/ueditconfig/', methods=['GET', 'POST'])
        def ueditconfig():
            # 导入地址
            from app import BASE_DIR
            # 获取请求动作
            action = request.args.get('action')
            result = {}
            # 读取配置文件
            if action == 'config':
            # 初始化时，返回配置文件给客户端
                with open(os.path.join(BASE_DIR,'static', 'ueditor', 'php',
                                       'config.json')) as fp:
                    try:
                        # 删除 `/**/` 之间的注释
                        CONFIG = json.loads(re.sub(r'\/\*.*\*\/', '', fp.read()))
                    except:
                        CONFIG = {}
                result = CONFIG

            # 文件上传
            if action  == 'uploadimage':
                upfile = request.files['upfile']  # 这个表单名称以配置文件为准
                # upfile 为 FileStorage 对象
                # 这里保存文件并返回相应的URL

                Suffix = upfile.filename.split('.').pop()
                filename = str(time.time())+str(random.randint(10000,99999))+'.'+Suffix
                imgurl = '/static/uploads/'+filename
                upfile.save(BASE_DIR+imgurl)

                result = {
                    "state": "SUCCESS",
                    "url": imgurl,
                    "title": filename,
                    "original":filename
                }

                print(BASE_DIR)

            return json.dumps(result)
