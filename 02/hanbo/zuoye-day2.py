#!/usr/bin/env python
#coding:utf-8
list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
for i in range(1,len(list)):
  for p in range(i+1,len(list)):
    if list[i] > list[p]:
      list[i],list[p] = list[p],list[i]

      
print list
