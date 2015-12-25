#!/usr/bin/env python
#encoding: utf-8

num_list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]


'''
方法一: 两次遍历
1. 第一次遍历找到最大的数字, 并记录到变量max_1中
2. 第二次遍历找到除max_1外的最大的数字, 并记录到max2中
'''

max_1 = 0
max_2 = 0

for num in num_list:
    if num > max_1:
        max_1 = num

for num in num_list:
    if num == max_1:
        continue
    if num > max_2:
        max_2 = num

print 'max_1:%d, max_2:%d' % (max_1, max_2)

'''
方法二: 一次遍历
1. 先拿出两个数字比较，将最大的赋值给max_1, 另一个赋值给max_2
2. 从第三个数字开始比较, 如果比max_1大(肯定比max_2大)
    a.将max_1的数字赋值给max_2
    b.将当前比较的值赋值给max_1
3. 如果比max_1小，比较是否大于max_2, 若大于, 将当比较值赋值给max_2
4. 如果比max_2小，则比较下一个值

'''


max_1 = 0
max_2 = 0

if num_list[0] > num_list[1]:
    max_1 = num_list[0]
    max_2 = num_list[1]
else:
    max_1 = num_list[1]
    max_2 = num_list[0]

for i in range(3, len(num_list)):
    if num_list[i] > max_1:
        max_2 = max_1
        max_1 = num_list[i]
    elif  num_list[i] > max_2:
        max_2 = num_list[i]

print 'max_1:%d, max_2:%d' % (max_1, max_2)
