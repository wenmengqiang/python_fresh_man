#学习条件
myage=20
if myage>18:
    print '你的年龄是',myage
    print u'成年'
elif myage==18:
    print "年方十八"    
else:
    print '你的年龄是',myage
    print '未成年'/n

#学习循环
names=['温梦强','赵珍珍',u'库里']
for mingzi in names:
    print mingzi

sum=0
for x in[1,2,3,4,5,6,7,8]:
    sum+=x
print sum

sum=0
for x in range(101):
    sum+=x
print sum
#目前的print，是在循环内执行的，缩进到行首，是在循环外   

#学习while循环
birth=raw_input('birth: ')
if  birth<2000:
    print '00pre'
else:
    print '00later'
#raw_input()只能读取字符串
