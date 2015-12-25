#!/usr/bin/python
# -*- encoding:utf-8 -*-
#
# 作业要求：
# 插入算法，排序
# 插入排序就是每一步都将一个待排数据按其大小插入到已经排序的数据中的适当位置，直到全部插入完毕
# 具体算法描述如下：
# 1. 从第一个元素开始，该元素可以认为已经被排序
# 2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
# 3. 如果该元素（已排序）大于新元素，将该元素移到下一位置
# 4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
# 5. 将新元素插入到该位置后
# 6. 重复步骤2~5
# 参考资料: http://bubkoo.com/2014/01/14/sort-algorithm/insertion-sort/

# 插入排序方法一
def insert_sort(my_list):
    print "The original list is %s" % my_list

    for i in range(1,len(my_list)):
        temp = my_list[i]
        while i > 0 and my_list[i-1] > temp:
            my_list[i] = my_list[i-1]
            i -= 1
        my_list[i] = temp

    print "After insert sort,the list is %s" % my_list

print "="*50+"solution 1"+"="*50
List1 = [12,3,1,21,2,2,3,4111,22,3333,45,33,45]
insert_sort(List1)

# 插入排序方法二
def insert_sort_2(my_list):
    print "The original list is %s" % my_list
    loop_count = 0

    for i in range(1,len(my_list)):
        start = i
        end = 0
        step = -1
        for idx in range(start,end,step):
            if my_list[idx] < my_list[idx-1]:
                my_list[idx],my_list[idx-1] = my_list[idx-1],my_list[idx]
                loop_count += 1
            else:
                break

    print "After insert sort,the list is %s" % my_list
    print "After insert sort,the loop count is %d" % loop_count

print "="*50+"solution 2 insert sort 2"+"="*50
List1 = [12,3,1,21,2,2,3,4111,22,3333,45,33,45]
insert_sort_2(List1)

# 选择排序(selection sort)
def selection_sort(my_list):
    print "The original list is %s" % my_list
    loop_count = 0
    temp_list = []

    for i in range(0,len(my_list)):
        list_min = min(my_list)
        temp_list.append(list_min)
        my_list.remove(list_min)
        loop_count += 1

    temp_list,my_list = my_list,temp_list
    print "After selection sort,the list is %s" % my_list
    print "After selection sort,the loop count is %d" % loop_count

print "="*50+"solution 3 selection sort"+"="*50
List1 = [12,3,1,21,2,2,3,4111,22,3333,45,33,45]
selection_sort(List1)

# 快速排序
def quick_sort(my_list,left,right):
    if left >= right or right < 2:
        return 1

    global loop_count_2
    storeindex = left
    pivot = my_list[right]

    for k in range(left,right):
        if my_list[k] < pivot:
            if k != storeindex:
                my_list[k],my_list[storeindex] = my_list[storeindex],my_list[k]
                loop_count_2 += 1
            storeindex += 1
    my_list[right],my_list[storeindex] = my_list[storeindex],my_list[right]

    quick_sort(my_list,left,storeindex-1)
    quick_sort(my_list,storeindex+1,right)

print "="*50+"solution 4 quick sort"+"="*50
loop_count_2 = 0
List1 = [12,3,1,21,2,2,3,4111,22,3333,45,33,45]
print "The original list is %s" % List1
quick_sort(List1,0,len(List1)-1)
print "After insert sort,the list is %s" % List1
print "After insert sort,the loop count is %d" % loop_count_2

# 各种排序数据交换次数对比结果，即以上程序的执行结果
==================================================solution 1 insert sort 1==================================================
The original list is [12, 3, 1, 21, 2, 2, 3, 4111, 22, 3333, 45, 33, 45]
After insert sort,the list is [1, 2, 2, 3, 3, 12, 21, 22, 33, 45, 45, 3333, 4111]
After insert sort,the loop count is 20
==================================================solution 2 insert sort 2==================================================
The original list is [12, 3, 1, 21, 2, 2, 3, 4111, 22, 3333, 45, 33, 45]
After insert sort,the list is [1, 2, 2, 3, 3, 12, 21, 22, 33, 45, 45, 3333, 4111]
After insert sort,the loop count is 20
==================================================solution 3 selection sort==================================================
The original list is [12, 3, 1, 21, 2, 2, 3, 4111, 22, 3333, 45, 33, 45]
After selection sort,the list is [1, 2, 2, 3, 3, 12, 21, 22, 33, 45, 45, 3333, 4111]
After selection sort,the loop count is 13
==================================================solution 4 quick sort==================================================
The original list is [12, 3, 1, 21, 2, 2, 3, 4111, 22, 3333, 45, 33, 45]
After insert sort,the list is [1, 2, 2, 3, 3, 12, 21, 22, 33, 45, 45, 3333, 4111]
After insert sort,the loop count is 5





'''
评注:
1. 不错，使用了不同的排序算法实现功能

加油
'''