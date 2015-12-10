#!/usr/bin/env python
a=[1,2,3,2,12,3,1,3,21,2,2,3,411,22,3333,444,111,4,5,777,65555,45,33,45]
for i in range(0,len(a)):
  for p in range(i+1,len(a)):
    max1 = a[i]
    max2 = a[p]
    if max1 < max2:
      a[i] = a[p]
      a[p] = max1
print a[0],a[1]
print a
