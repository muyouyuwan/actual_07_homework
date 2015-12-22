#!/usr/bin/python
#-*- coding: utf-8 -*-

def sortList(argvlist):
    """This function is used to sort list by insertion algorithm"""
    try:
        if type(argvlist) != list or len(argvlist) < 2:
            print('The parameter must be list and the list length is larger than 1!') 
        else:
            #Insertion algorithm
            for i in range(1,len(argvlist)):
                contrast = argvlist[i]
                while i > 0 and int(contrast) < int(argvlist[i-1]):
                    argvlist[i] = argvlist[i-1]
                    i -= 1
                argvlist[i] = contrast
            print(argvlist)
            
    except:
        print('The list exist a element not a number!')
        return -1

temp_list = [1,2,3,2,12,3,1,3,21,2,2,3,65555,4111,22,3333,444,111,4,5,777,65555,45,33,45]
sortList(temp_list)



'''
流程:
1. 从argvlist索引为1的元素从左到右遍历
2. 依次比较当前遍历元素前的元素，如果比当前元素大，则向后移动，知道比较的元素不小于（大于或等于）当前元素，或无元素比较时结束比较，并将遍历元素插入当比较元素位置后或list头
3. 重复1, 2步骤

评注:
1. 排序结果正确
2. 定义函数的方式实现功能, 并对列表进行相应检查，使用异常处理
3. 借助constast变量使用的插入排序算法


加油
'''
