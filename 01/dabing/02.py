#encoding:utf-8

def  inser_sort():
	arr = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
	for i in range(len(arr)):   ##遍历list
		min_in = i             ##定义list中最小的数对应的索引
		for j in range(i+1,len(arr)):   ##从第i+1个数开始遍历索引
			if arr[min_in] >  arr[j]:   ##如果最小索引对应的数比后面的数大，那么就把索引值赋给最小值的索引
				min_in = j
		arr[min_in],arr[i] = arr[i],arr[min_in]               ##索引对应的值互换位置
	print arr 

inser_sort()