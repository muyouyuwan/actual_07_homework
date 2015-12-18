
#!/usr/bin/env python2.7
#encoding: utf-8
list = [23,32,1,234324,234324,6435,3432,6425,22,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max1_num = 0
max2_num = 0
for num in list:
    if num >= max1_num:
        max1_num = num
for num in list:
    if num == max1_num:
        continue
    elif num >= max2_num:
        max2_num = num
print max1_num
print max2_num