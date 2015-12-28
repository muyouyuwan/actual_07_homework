#!/usr/bin/env python
iteams=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
tmp_first=''
tmp_second=''
for x in iteams:
    if tmp_first == '':
       tmp_first = x
    elif x >= tmp_first:
             tmp_second = tmp_first 
             tmp_first = x
print "The biggest number in the list are ( %d  %d )" % (tmp_first, tmp_second)  
