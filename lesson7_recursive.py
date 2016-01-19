# -*- coding: utf-8 -*-
#递归函数，在函数内部条用自身，这就是递归函数
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print fact(1)
print fact(20)
#print fact(1000)
#在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，也就是说一个栈中能放栈帧多少是有限的（Windows的一个栈的大小为2M），所以，递归调用的次数过多，会导致栈溢出。如果不想溢出，使用堆，现在还没讲到

#防止该函数栈溢出，改成“尾递归方式”，把每一步的成绩传入到递归函数中
#以下为我理解的尾递归方式，这跟上面的没区别
#def fact(n):
#    if n==1:
 #       return 1
#    else:
#        n*=fact(n-1)
#    return n

#print fact(2)
#print fact(1000)
#得到提示后的方法2
#def fact_liter(n):
#    return n*fact(n-1)
    
#def fact(n):
#    if n==1:
#        return 1
#    return fact_liter(n)    

#print fact(3)
#print fact(1000)

#主要的解决方法是吧每一步的乘积传入到递归函数中，因为没有直接返回递归函数本身
def fact(n):
    return fact_liter(n,1)

def fact_liter(num,product):
    if num==1:
        return product
    return fact_liter(num - 1,num * product)

print fact(1000)
#是不是可以理解为，多次调用函数，多用调用栈，而不是不停的调用递归
#草，还是不行


