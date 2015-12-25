#!/usr/bin/env python
#-*- coding:utf-8 -*-

number_list = [1, 2, 3, 2, 12, 3, 1, 3, 21, 2, 2, 3, 4111,22, 3333, 444, 111, 4, 5, 777, 65555,1]
for i in range(1, len(number_list)):      
    for o in range(0, i):                
        if number_list[i] < number_list[o]:
            number_list[i], number_list[o] = number_list[o], number_list[i]
            
print number_list

'''
流程:
1. 从number_list索引为1的元素从左到右遍历
2. 从number_list开始遍历每一个元素并比较当前元素的大小, 若大于当前元素将当前遍历元素和比较元素交换, 比较完成后保证遍历元素和其之前的元素是一个有序列表
3. 重复1, 2步骤

评注:
1. 排序结果正确
2. 使用了插入算法排序

加油

'''
