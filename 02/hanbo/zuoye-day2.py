#!/usr/bin/env python
#coding:utf-8
list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
for i in range(1,len(list)):
  for p in range(i+1,len(list)):
    if list[i] > list[p]:
      list[i],list[p] = list[p],list[i]

      
print list


'''
流程:
1. 从list_1索引为1的元素开始遍历每一个元素
2. 找到从遍历元素后到遍历list, 当遍历的元素小于当前元素则进行交换, 最终将最小的元素换到当前遍历的位置
3. 重复1, 2步骤

评注:
1. 对于本次示例的排序结果正确，但是如果list的第一位不是list中最小的元素时排序结果错误, 第一个for循环应该从第0位开始遍历
2. 使用类选择排序算法实现

改进:
1. 定义变量避免使用关键字和已经内置的标识符list
2. 第2个循环是为了找到从遍历元素开始到list结束最小的元素，并交换到当前要排序元素位置，那可不可以先定义比较出最小的数字的索引，如果索引和当前要排序的元素索引相同就不交换，如果不同，则交换，可一个达到目的，这样就最多进行一次交换


num_list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]  # 修改变量名避免使用关键字和内置的标识符
for i in range(0,len(num_list)):  # 从0开始遍历
    for p in range(i+1, len(num_list)):
        if num_list[i] > list[p]:
            num_list[i], num_list[p] = num_list[p], num_list[i]

print num_list


num_list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
for i in range(0,len(num_list)):
    min_i = i
    for p in range(i+1, len(num_list)):
        if num_list[min_i] > list[p]:
            min_i = p   #找到一个更小的就将索引赋值给min_i, 这样就能找到从i到结束最小元素的索引

    if min_i != i: #若当前遍历元素不是最小，则将最小元素交换到当前i的位置
        num_list[i], num_list[min_i] = num_list[min_i], num_list[i]

print num_list


加油
'''
