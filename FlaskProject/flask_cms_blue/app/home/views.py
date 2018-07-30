from . import home
from flask import request,render_template,redirect,url_for,session,abort
from app.models import Users,db,Types,Article,Ats,Tags
# python 的md5加密模块
import hashlib,os,json,time,re,random

# 在处理请求前运行的函数，类似于Django中的中间件
@home.before_request
def check_login():
    # 判断是否去要登录的页面
    urllist = ['/write/']
    if request.path in urllist:
        # 判断是否登录
        if not session.get('VipUser',None):
            return redirect(url_for('home.login'))

# 主页
@home.route('/')
def index():
    all_artile_data = db.session.query(Article,Types,Users).filter(Article.type_id==Types.id).filter(Users.id==Article.uid).order_by(Article.addtime.desc()).all()
    return render_template('home/index.html',art=all_artile_data)

# 文章详情
@home.route('/<name>/p/<aid>/')
def articleinfo(name,aid):
    # 查询文章，文章分类，文章作者
    article = db.session.query(Article,Types,Users)\
        .filter(Article.type_id==Types.id)\
        .filter(Article.uid==Users.id)\
        .filter(Article.id==aid).first()
    # 查询文章标签
    tag = db.session.query(Tags,Ats)\
        .filter(Ats.article_id==aid)\
        .filter(Tags.id==Ats.tags_id).all()
    return render_template('home/myblog/info.html',article=article,tag=tag)


# 我的博客
@home.route('/<name>/')
def myblog(name):
    u = Users.query.filter_by(name=name).first_or_404()
    # 查找该同学的所有博文,标签，及其关系
    article_data = db.session.query(Article,Types).filter(Article.uid == u.id).filter(Article.type_id==Types.id).all()
    return render_template('home/myblog/index.html',uinfo=u,article_data=article_data)

# 发布新博文
@home.route('/write/',methods=['POST','GET'])
def write():
    if request.method == 'GET':
        return render_template('home/myblog/add.html')
    elif request.method == 'POST':
        try:
            # 添加文章
            a = Article()
            a.title = request.form['title']
            a.context = request.form['content']
            a.type_id = request.form['pid']
            a.uid = session['VipUser']['uid']
            db.session.add(a)
            db.session.commit()
        except:
            db.session.rollback()
            return '文章添加失败'

        try:
            # 添加标签
            ts = request.form['tags'].split(',')
            tagsarr = []
            for x in ts:
                # 判断数据库是否存在tags标签
                tags = Tags.query.filter_by(tagname=x, uid=session['VipUser']['uid']).first()
                if tags:
                    # 判断当前标签如果已经存在,则直接获取id
                    tagsarr.append(tags.id)
                else:
                    # 如果不存在,则添加到数据库,获取id
                    t = Tags()
                    t.uid = session['VipUser']['uid']
                    t.tagname = x
                    db.session.add(t)
                    db.session.commit()
                    tagsarr.append(t.id)
        except:
            db.session.rollback()
            return '标签创建失败'

        try:
            # # 搞定 标签和文章关系
            for x in tagsarr:
                at = Ats()
                at.article_id = a.id
                at.tags_id = x
                db.session.add(at)
                db.session.commit()
        except:
            db.session.rollback()
            return '标签和文章关系创建失败'

        uname = session['VipUser']['uname']
        return '<script>alert("文章发布成功");location.href="/' + uname + '/"</script>'

# 获取分类
@home.route('/gettypes/<pid>/')
def gettypes(pid):
    # 根据查询分类
    ts = Types.query.filter_by(pid=pid).all()
    # 将对象列表重组为字典列表，以json格式传过去
    arr = []
    for x in ts:
        data = {'id': x.id, 'tname': x.tname, 'pid': x.pid}
        arr.append(data)
    jsts = json.dumps(arr)
    return jsts

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
                               'config.json'),encoding="utf-8") as fp:

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
    return json.dumps(result)

# 注册
@home.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('home/login/register.html')
    elif request.method == 'POST':

        u = Users()
        u.name = request.form['username']
        u.pwd = u.md5password(request.form['password'])
        u.email = request.form['email']
        db.session.add(u)
        db.session.commit()

        return redirect(url_for('home.login'))

# 登录
@home.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('home/login/login.html')

    elif request.method == 'POST':
        u = Users.query.filter_by(name=request.form['username']).first()
        # 用户判断
        if u:
            # 密码判断
            if u.checkpassword(request.form['password']):
                session['VipUser'] = {'uid':u.id,'uname':u.name}
                return '<script>alert("登录成功");location.href="/"</script>'

        return '<script>alert("用户名或密码不正确");location.href="/login"</script>'

# 退出登录
@home.route('/logout/')
def logout():
    session['VipUser'] ={}
    return redirect(url_for('home.index'))


# 自定义404页面
@home.errorhandler(404)
def two(error):
    return render_template('404.html'),404

