#!/usr/bin/env python
list1=[] 

while  True:
        user_input = raw_input('please input number:')
        if user_input=='':
                 print  'can not input empty'
                 continue
        list1.append(user_input)
        if  len(list1) >1:
                start= len(list1)-1
                end =0
                step =-1
                for j in range(start,end,step):
                        if list1[j] < list1[j-1]:
                                list1[j],list1[j-1]=list1[j-1],list1[j]
        print list1
