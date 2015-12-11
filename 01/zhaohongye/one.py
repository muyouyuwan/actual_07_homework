#coding:utf-8
Max_number = 0
number2 = 0
list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,    444,111,4,5,777,65555,45,33,45]
for i in list:
    if i > Max_number:
      Max_number = i
for i in list:
    if  i < Max_number and i > number2:
       number2 = i
print '序列中最大的两个值为: %s and %s' % (Max_number,number2)
