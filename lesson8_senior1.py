# -*- coding: utf-8 -*-
#构造一个2，4，6，。。。。100的列表，可以通过循环实现
Num=[2]
while Num[-1]<100:
    Num.append(Num[-1]+2)
print Num

#以下是书中示例
L=[]
n=1
while n<=99:
    L.append(n)
    n=n+2

#再次学习切片
L=['Michael','Bob','Homels','Watson']
print L[0:3]
print L[:3]
#前十个数每两个取一个
print Num[:10:2]
#所有书每五个取一个
print Num[::5]

#学习迭代
for key in Num:
    print key

for key in 'AbC':
    print key

#如何判断一个对象是可迭代对象，通过collections模块的Iterable类型判断
from collections import Iterable
print isinstance('abc',Iterable)
print isinstance(123,Iterable)

#打印list中的下表
for i,key in enumerate(L):
    print i,key

#学习列表生成式ListComprehension
Num1=range(1,12)
print Num1

#生成1×1 2×2....10×10
Num1=[]
for x in range(1,11):
    Num1.append(x*x)
print Num1
#列表生成式的办法更简单.这是一个Python内置的非常简单却强大的可以用来创建list的生成式。
print [x*x for x in range(1,11)]
#for循环后面加上if判断，筛选出仅偶数的平方。×××××××××××rang函数×××××××
print [x*x for x in range(1,11) if x%2==0]
#两次循环生成全排列
print [m+n for m in 'ABC' for n in 'abc']
#列出当前目录下的所有文件和目录名
import os #导入os模块
print [d for d in os.listdir('.')]
#for循环其实可以同时使用两个甚至多个变量，比如dict
d={'x':'a','y':'b'}
for k,v in d.iteritems():
    print k,'=',v
#使用两个变量来生成list，×××××××××××iteritem函数×××××××
print [k+'='+v for k,v in d.iteritems()]
#把一个list中的字符串全部变成小写
print [s.lower() for s in L]
print isinstance('abc',str)

#学习生成器。在面对大量列表元素的时候，若列表元素可以通过一定的规则推算大部分的元素，这种一边演算一遍循环的机制，成为生成器,generator
print [x*x for x in range(10)]
#print (x*x for x in range(10))
g=(x*x for x in range(10))
for x in g:
    print x


