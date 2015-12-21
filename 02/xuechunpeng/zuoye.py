nu_li = [4,3,2,1]

for i in range(1,len(nu_li)):
    start = i
    end = 0
    step = -1
    for idx in range(start,end,step):
        if nu_li[idx] < nu_li[idx - 1]:
            nu_li[idx],nu_li[idx - 1] = nu_li[idx - 1],nu_li[idx]
        else:
            break
print nu_li
    

'''
流程:
1. 从nu_li索引为1的元素从左到右遍历每一个元素
2. 比较当前遍历的元素和前面的每个元素进行比较，如果比前面的数字小，则进行交换，再和交换后前面的元素进行比较，直到不小于前面的元素或者已经没有元素可以比较，就结束本次排序
3. 重复1,2步骤

评注:
1. 排序结果正确
2. 使用了插入算法实现list从小到大排序

加油
'''