# -*- coding: utf-8 -*-
print '中文测试正常'
print u'Hi,%s' % u'Michael'

#学习list和tuple，tuple不可变
classmates=['Wing','温梦强','Dreamworks','赵珍珍','Golden State Warriors']
print classmates
print '长度是',len(classmates)
print '第二个变量是',classmates[1]
print '最后一个变量是',classmates[-1]

#添加元素使用insert函数，必须使用u前缀可插入中文字符串
classmates.insert(1,u'爸爸')
print '第二个变量是',classmates[1]

#删除元素使用pop
classmates.pop(1)
print '第二个变量是',classmates[1]

#替换元素
classmates[1]=u'爸爸'
print '第二个变量是',classmates[1]

number=('Michael','温梦强','Tracy')
print number

