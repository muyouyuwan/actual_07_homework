#!/usr/bin/env python

list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
b = 0
c = 0
for i in list:
    if i > b:
        b = i
for o in list:
    if o < b and o > c:
        c = o
print "max=%s, max2=%s" %(b,c)
        
        

