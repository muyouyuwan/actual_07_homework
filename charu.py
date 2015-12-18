#!/usr/bin/python
#coding:utf-8
#求列表l1的最大的2个值
l1 = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]


_count = 0
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        _count+=1
        if l1[i] > l1[j]:
            l1[i],l1[j] = l1[j],l1[i]
    
print l1
#print _count

