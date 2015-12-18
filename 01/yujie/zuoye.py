#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# 作业要求：
# 一个序列[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
# 求这个list的最大的两个值
# 先实现基本功能，实现之后，多考虑一些异常情况，如:
# 1.最大的两个数相等;
# 2.序列只有一个元素;
# 3.能否输出最大值的索引值;
# 4.优化变量命名，拆分函数和模块等；

# solution 1
print "="*50+"solution 1"+"="*50
List1 = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max_num_1 = 0
max_num_2 = 0
for i in List1:
    if i > max_num_2:
        if i > max_num_1:
            max_num_2 = max_num_1
            max_num_1 = i
        else:
            max_num_2 = i

print "The original list is: %s" % List1
print "In the list the max two numbers are %d %d" % (max_num_1,max_num_2)

# solution 2
print "="*50+"solution 2"+"="*50
def max_top2_list(list):
    if len(list) < 2:
        print "Please input a list having two more items."
        return 1

    max_num_1 = 0
    max_num_2 = 0
    for i in list:
        if i > max_num_2:
            if i > max_num_1:
                max_num_2 = max_num_1
                max_num_1 = i
            else:
                max_num_2 = i

    print "The original list is: %s" % list
    print "In the list the max two numbers are %d %d" % (max_num_1,max_num_2)
List2 = [777]
max_top2_list(List2)

# solution 3
print "="*50+"solution 3"+"="*50
def max_top2_list(list):
    if len(list) < 2:
        print "Please input a list having two more items."
        return 1

    max_num_1 = 0
    max_num_2 = 0
    for i in list:
        if i >= max_num_2:
            if i >= max_num_1:
                max_num_2 = max_num_1
                max_num_1 = i
            else:
                max_num_2 = i

    print "The original list is: %s" % list
    print "In the list the max two numbers are %d %d" % (max_num_1,max_num_2)
List3 = [777,45,89,348,777,3,6,19]
max_top2_list(List3)

# solution 4
print "="*50+"solution 4"+"="*50
def max_top2_list(list):
    if len(list) < 2:
        print "Please input a list having two more items."
        return 1

    max_num_1 = 0
    max_num_2 = 0
    max_num_1_index = 0
    max_num_2_index = 0

    for i in range(0,len(list)):
        if list[i] >= max_num_2:
            if list[i] >= max_num_1:
                max_num_2 = max_num_1
                max_num_1 = list[i]
                max_num_2_index = max_num_1_index
                max_num_1_index = i
            else:
                max_num_2 = list[i]
                max_num_2_index = i

    print "The original list is: %s" % list
    print "In the list the max two numbers are List[%d]:%d,List[%d]:%d" % (max_num_1_index,max_num_1,max_num_2_index,max_num_2)
List4 = [777,45,89,348,777,3,6,19,777]
max_top2_list(List4)

# solution 5
print "="*50+"solution 5"+"="*50
def max_top2_list(list):
    if len(list) < 2:
        print "Please input a list having two more items."
        return 1

    sort_list=list[:]

    for i in range(0,len(sort_list)):
        for j in range(i+1,len(sort_list)):
            if sort_list[i] < sort_list[j]:
                sort_list[i],sort_list[j]=sort_list[j],sort_list[i]

    print "The original list is: %s" % list
    print "The after sort list is: %s" % sort_list
    print "In the list the max two numbers are %d,%d" % (sort_list[0],sort_list[1])
List5 = [777,45,89,348,777,3,6,19,777,889]
max_top2_list(List5)