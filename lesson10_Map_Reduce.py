# -*- coding: utf-8 -*-
#函数式编程学习
def add(x,y,f):
    return f(x)+f(y)
print add(5,6,abs)
#把abs函数指向f变量

#高阶函数map函数，接受两个参数，一个是函数，一个是序列。比如接受函数f（x）=x×x，同时接受序列[1,2,3~~~10],返回的结果为新的序列
def f(x):
    return x*x

print map(f,[1,2,3,4,5,6,7])

#与以下代码对比
L=[]
for n in [1,2,3,4,5,6,7]:
    L.append(f(n))
print L

#对比结果，map函数更抽象化，以下函数更直观，更易懂
print map(str,[1,2,3,4,5,6,7,8,9])

#高阶函数reduce（函数，序列），reduce函数把序列中的每一个元素进行函数计算。
def add(x,y):
    return x+y
print reduce(add,[1,3,5,7,9])

def fn(x,y):
    return x*10+y
print reduce(fn,[1,3,5,7,9])

def fn(x,y):
    return x*10+y
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10}[s]
print map(char2num,'1111111111111111a')
print reduce(fn,map(char2num,'12357'))
#char2num函数的作用原理是什么，为什么使用map后返回值是字符对应的数字。看来字典的作用没有掌握，,直接将对应的字符指定到对应的值，这下对字典的理解深刻了
#以下整理为str2int的函数
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10}[s]
    return reduce(fn,map(char2num,s))
print str2int('a1a2')
#以下为使用lambda函数进一步简化
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10}[s]
def str2int(s):
    return reduce(lambda x,y: x*10+y,map(char2num,s))
print str2int('3a3')

#练习题：一，利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。二，Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。
def Cap1stLetter(s):
#    def lower(s):
#        return {'A':a,'B':b,'C':c,'D':d,'E':e,'F':f,'G':g,'H':h,'I':i,'J':j,'K':k,'L':l,'M':m,'N':n,'O':o,'P':p,'Q':q,'R':r,'S':s,'T':t,'U':u,'V':v,'W':w,'X':x,'Y':y,'Z':z,'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'q':q,'r':r,'s':s,'t':t,'u':u,'v':v,'w':w,'x':x,'y':y,'z':z}[s]    
#    def upper(s):
#        return {'a':A,'b':B,'c':C,'d':D,'e':E,'f':F,'g':G,'h':H,'i':I,'j':J,'k':K,'l':L,'m':M,'n':N,'o':O,'p':P,'q':Q,'r':R,'s':S,'t':T,'u':U,'v':V,'w':W,'x':X,'y':Y,'z':Z}[s]
    s1=s[1:].lower()
    s2=s[0].upper()
    return s2+s1

print map(Cap1stLetter,['adam', 'LISA', 'barT'])
    
#编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(x,y):
    return x*y
print reduce(prod,[1.,3,4,5,6])              

