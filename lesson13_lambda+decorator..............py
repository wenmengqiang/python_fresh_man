# -*- coding: utf-8 -*-
#本节学习匿名函数lambda，这种函数不需要显式的定义函数，可直接传入匿名函数.匿名函数只能有一个表达式，返回值就是表达式的结果
print map(lambda x: x*x,[1,2,3,4,5,6,7])
#lambda x: x*x
#def f(x):
#   return x*x
f=lambda x: x*x
print f
print f(5)
def build(x,y):
    return lambda:x*x+y*y

#学习装饰器
def now():
    print '2015-12-14'
f=now
f()
print f()
#cmd中再次输出一个None，函数对象有一个__name__属性，可以拿到函数的名字
print now.__name__
f()
print f.__name__

#在代码运行期间动态增加功能的方式，称之为Decorator，他是一个返回函数的高阶函数
def log(func):
    def wrapper(*args,**kw):
        print 'call %s()' %func.__name__
        return func(*args,**kw)
    return wrapper
@log
def now():
    print '2015-12-14'
now()
#以上函数相当于执行了下面一行 now=log(now)

#如果decorator本身需要传参，那就编写一个返回decorator的高阶函数，写出来更复杂。比如，要自定义log的文本
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print '%s %s():' %(text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print '2015-12-14'
now()
print now.__name__

#一个完整的decorator的写法如下
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print 'call %s():' % func.__name__
        return func(*args,**kw)
    return wrapper
#或者针对带参数的decorator
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print '%s %s():' %(text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator

#习题一，请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print '%s%s():' %(text,func.__name__)
            #无用print 'end call %s()' %func.__name__
            return func(*args,**kw)
            #无用print 'end call %s()' %func.__name__
        return wrapper
        #无用print 'end call %s()' %func.__name__
    return decorator
    #无用print 'end call %s()' %func.__name__
@log('begin call \n')
def now():
    print '2015-12-14-16:27'
    print 'end call'
now()
#习题二，能否写出一个@log的decorator，使它既支持一下代码：
#@log
#def f():
#    pass
#×××××××××××××××××××××××××××
#@log('execute')
#def f():
#pass
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print '%s %s():' %(text,func.__name__)            
            return func(*args,**kw)            
        return wrapper        
    return decorator    
@log
def f():
    print 'i am here'
f()
#line95注释func=''的话，上面这个函数根本没有执行，就谈不上支持了。
#那么现在问题来了，到底func这个参数是从哪里传进来的，
@log('execute')
def f():
    pass
f()

