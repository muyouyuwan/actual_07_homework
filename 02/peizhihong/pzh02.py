# coding:utf-8

# pzh02.py-插入排序

def charuSort(lst):
	nloops = len(lst)
	for i in range(1, nloops):
		for j in range(i, 0, -1):
			if lst[j-1] > lst[j]:
				lst[j-1], lst[j] = lst[j], lst[j-1]
			else:
				break
	return lst

def main():
	lst = [5, 6, 3, 1, 8, 7, 2, 4]
	ordLst = charuSort(lst)
	print ordLst

if __name__ == '__main__':
	main()



'''
流程:
1. 从lst索引为0的元素开始从左到右遍历每一个元素
2. 比较当前遍历的元素和其前面的元素，如果比前面的数字小，则进行交换，在和交换后前面的元素进行比较，直到不小于前面的元素或者已经没有元素可以比较，就结束本次排序
3. 重复1, 2步骤

评注:
1. 排序结果正确
2. 定义函数的方式实现插入排序
3. 使用了文件脚本启动name判断执行脚本

加油
'''

