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

# solution 1
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