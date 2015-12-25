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


'''
流程:
1. 每次让用户输入一个字符
2. 将用户输入则字符append到list1中
3. 从list1最后一个元素逐个与前一个元素比较，若小于前面进行交换, 再和交换后的前一位比较，直到比较晚列表中的元素
4. 重复1, 2,3步骤

评注:
1. 排序结果正确
2. 使用了插入算法实现list从小到大排序
3. 从控制台每次接收用户输入，并插入到list的正确位置

改进:
1. 在用户输入后将字符串转化为数字
2. 将一个已经存在的列表进行插入排序

加油
'''
