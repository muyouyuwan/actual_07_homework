#!/usr/bin/env python
#-*- coding:utf-8 -*-

number_list = [1, 2, 3, 2, 12, 3, 1, 3, 21, 2, 2, 3, 4111,22, 3333, 444, 111, 4, 5, 777, 65555,1]
for i in range(1, len(number_list)):      
    for o in range(0, i):                
        if number_list[i] < number_list[o]:
            number_list[i], number_list[o] = number_list[o], number_list[i]
            
print number_list
