#!/usr/bin/python
#-*- coding: utf-8 -*-

temp_list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
len_list = len(temp_list)
while len_list:
    for i in range(len_list-1):
        if temp_list[i] > temp_list[i+1]:
            t = temp_list[i]
            temp_list[i], temp_list[i+1] = temp_list[i+1], t
    len_list -= 1
print('The two maximum number are "%s" and "%s"!' % (temp_list[-2], temp_list[-1]))
