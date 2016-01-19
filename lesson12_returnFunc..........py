# -*- coding: utf-8 -*-
#函数作为返回值
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum
print lazy_sum(1,2,3)
f=lazy_sum(1,2,3,4)
print f()

#当一个函数返回了一个函数后，其内部的局部变量还被新函数引用。
def count():
    fs=[]
    for i in range(1,2):
        def f():
            return i*i
        fs.append(f)
        print f()
    return fs
f1=count()
#在上面的时候，
#返回函数不要引用任何循环变量，或者后续会发生变化的变量
print f1()
#当前错误产生的原因不清楚.print打印的时候到底调用的是什么，为什么f1 f2 f3一起执行的时候，就可以打印
#print f2()
#print f3()

#在返回函数中一定要引用循环变量，方法是再创建一个函数，用该函数的参数绑定循环变量当前的值
def count():
    fs=[]
    for i in range(1,4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
    return fs
f1,f2,f3=count()
