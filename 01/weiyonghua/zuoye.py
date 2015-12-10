#!/usr/bin/env python

list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,21121]
max1=0
max2=0
for i in list:
   if max1 < i:
       max1=i
for k in list:
   if k < max1  and  max2 < k:
      max2=k
print 'max_1  is %s and max_2 is %s' %(max1,max2)
