# -*- coding: utf-8 -*-
#高阶函数，filter也接受一个函数和一个序列，把函数依次作用于每个元素，然后根据返回值决定True保留还是False丢弃该元素
def is_odd(n):
    return n%2==1
print filter(is_odd,[1,2,4,5,67])

#把一个序列中的空字符删掉
def not_empty(s):
    return s and s.strip()
print filter(not_empty,['a','',None])

#用filter()删除1~100的素数
def is_prime(s):
    n=2
    while n<s: 
        if s%n==0:
            return False
            pass
        else:
            n+=1
    if n==s:
        return True 
print filter(is_prime,range(1000))

#高阶函数，sorted函数可以对list进行排序
print sorted([36,5,32,12,21])

#自定义一个reverse_cmp函数
def reversed_cmp(x,y):
    if x>y:
        return -1
    if x<y:
        return 1
    return 0
print sorted([36,12,23,1,4],reversed_cmp)
print sorted(['wing','Zhao','zhenzhen','Mengqiang'],reversed_cmp)

#忽略大小写，按照字母序排序
def cmp_ignore_cast(s1,s2):
    u1=s1.upper()
    u2=s2.upper()
    if u1<u2:
        return -1
    if u1>u2:
        return 1
    return 0
print sorted(['wing','Zhao','zhenzhen','Mengqiang'],cmp_ignore_cast)
