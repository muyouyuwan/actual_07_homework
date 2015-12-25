#!/usr/bin/python
#coding:utf-8
#求列表list_1的最大的2个值

list_1 = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

## 方法一
max_1 = 0
max_2 = 0
for i in list_1:
    if i > max_1:
        max_1 = i
for j in list_1:
    if j != max_1 and j > max_2:
        max_2 = j
print "方法一：max_1 is %s, max_2 is %s" % (max_1,max_2)


## 方法二
max_1 = 0
max_2 = 0

for num in list_1:
    if num > max_1:
        max_2 = max_1
        max_1 = num
    elif num > max_2:
        max_2 = num
print "方法二：max_1 is %s, max_2 is %s" % (max_1,max_2)
