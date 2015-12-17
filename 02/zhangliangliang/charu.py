#!/usr/bin/python
#coding:utf-8
#插入排序

# 方法一
l1 = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
_count = 0

for i in range(0,len(l1)):
    for j in range(i+1,len(l1)):
        _count+=1
        while l1[i] > l1[j]:
            l1[i],l1[j] = l1[j],l1[i]
print l1
print _count

# 方法二
l2 = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
_count2 = 0

for i in range(1,len(l2)):
    num = l2[i]
    j = i - 1
    while j >= 0 and l2[j] > num:
        _count2 += 1
        l2[j+1],l2[j] = l2[j],num
        j -= 1
print l2
print _count2
