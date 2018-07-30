from functools import wraps

def logged(f):
    @wraps(f)
    def log(*args,**kwargs):
        '''我是log'''
        print(f.__name__ ,'被调用了')
        return f(*args,**kwargs)
    return log

@logged
def foo():
    '''文档'''
    print('我是foo函数')

foo()

print(foo.__name__)
print(foo.__doc__)