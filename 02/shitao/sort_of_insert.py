#!/usr/bin/env python
#coding=utf-8
arr = [2,5,3,1,33,2,12,45,23,12,546,-1,9,900,-100,33,44,22]
for i in range(1,len(arr)):
    if arr[i] < arr[i-1]:
        temp = arr[i]	 # 定位比已排序数字小的数字 ，斌赋值临时变量
        
	for j in range(i)[::-1]: # 将定位数字的索引值倒序，依次向前循环比较
	    if arr[j] > temp:
                arr[j],arr[j+1] = arr[j+1],arr[j] # 如果当前值比前一个值大，值互相交换
	
	    else:		#  如果小于或者等于，跳过循环
	        
		continue
print "the sorted list is %s" %arr
