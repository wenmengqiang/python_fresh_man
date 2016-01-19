# -*- coding: utf-8 -*-
print abs(10.11)

def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

#返回多个值
import math

def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
print move(100,100,60,math.pi/6)

#num=raw_input('请输入要求绝对值的数字：\n')
#s= my_abs(x)
#print s
#再次犯错误，raw_input处理后变成字符串，这时候使用求绝对值，是不会有任何改变的
#一下是修改
#num=int(raw_input('enter the number:\n'))
#s= my_abs(num)
#print s

print cmp(1,2)

def nop():
    pass
#这个代码就是占个茅坑

def enroll(name,gender):
    print 'name',name
    print 'gender',gender

print enroll('sarah','f')
#为什么会输出None??????????

def power(x):
    x*=x
    return x
print power(9)

def power(x,n):
    s=1
    while (n>=1):
        n-=1
        s*=x
    return s
print power(9,3)
#print power(9)  这个函数现在不能用，因为少一个参数

def power(x,n=2):
    s=1
    while(n>0):
      n-=1
      s*=x
    return s
print power(9)

#默认参数的大坑演示
def add_end(L=[]):
    L.append('END')
    return L

print  add_end([1,2,3])
print add_end()
print add_end()
print add_end([1,2,3])
#多次执行add_end()后，会自动垂加end，所以，定义默认参数要牢记一点：默认参数必须指向不变对象None

def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L
print add_end()
print add_end()
#与上一次两个add_end()函数执行的结果不同

#可变参数
def calc(nums):
	sum=0
	for n in nums:
		sum+=n*n
	return sum	

print calc([1,2,3])
print calc((1,2,4))
#以上是正常的调用方式，其实还是一个参数，不过参数是list或者tuple

def calc(*nums):
	sum=0
	for n in nums:
		sum+=n*n
	return sum

#print calc([1,2,3])这是不行的
print calc(1,2,5)
num1=[1,2,3]
print calc(num1[0],num1[1],num1[2])
#上面这种方法太繁琐
print calc(*num1)

#关键字参数学习
def person(name,age,**kw):
	print 'name:',name,'age',age,'other',kw
person('Machiael',30)
person('Bob',35,city='Beijing')
person('Adam',45,gender='M',job='Engineer')

kw={'city':'Beijing','job':'Engineer'}
person('Jack',24,**kw)

#参数组合学习，在python中定义函数，可以用必选参数、默认参数、可变参数和关键词参数
#但顺序必须是：必选参数、默认参数、可变参数和关键词参数
def func(a,b,c=0,*args,**kw):
	print'a',a,'b=',b,'c=',c,'args=',args,'kw=',kw

print func(1,2)
print func(1,2,3)
print func(1,2,c=3)
print func(1,2,3,'a','b')
print func(1,2,3,'a','b',x=99)
#此处不停再次输出一个None????????
args=(1,2,3,4)
kw={'x':98}
print func(*args,**kw)
#此处再次输出一个None？？？？？？
#使用普通函数candidate的时候，在cmd中会输出一个None表示结束？？？？








