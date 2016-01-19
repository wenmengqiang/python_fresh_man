# -*- coding: utf-8 -*-
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print b
        a,b=b,a+b
        n=n+1
#非波拉契数列的普通定义方式
#fib(6)

def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
for x in fib(6):
    print x
#非波拉契的generator方式

def odd():
    print 'step1'
    yield 1
    print 'step2'
    yield 3
    print 'step3'
    yield 5
o=odd()
for x in o:
    print x
odd()
#把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。其实不是很会用


