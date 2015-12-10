#!/usr/bin/python
#coding:utf-8
#求列表l1的最大的2个值
l1 = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

max1 = 0
max2 = 0
for i in l1:
    if i > max1:
        max1 = i
    else:
        continue
#    print max1,max2
    for j in l1:
        if j < max1 and j > max2:
            max2 = j

print "max1 is %s, max2 is %s" % (max1,max2)
