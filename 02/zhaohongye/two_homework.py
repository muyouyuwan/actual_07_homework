#encoding:utf-8
#插入算法  
num_list = []
while True:
	inputa = raw_input('plz input some number ： ')
	str1 = inputa
	if str1.isdigit() == True :
		num_list.append(inputa)
	elif str1.isdigit() == False:
	    if inputa == 'quit':
	    	print num_list
	    	break
	    else:
	    	print 'plz input some number ! ! !'
	for i in range(1,len(num_list)):
		start = i
		end = 0
		step = -1
		for idx in range(start,end,step):
			if num_list[idx] < num_list[idx - 1]:
				num_list[idx],num_list[idx - 1] = num_list[idx - 1],num_list[idx]
			else:
				break
	print num_list



'''
流程:
1. 从控制台接收用户输入，进行数字判断并加入到num_list中，如果用户输入错误给提示，可以退出 
2. 从num_list索引为1的元素从左到右遍历每一个元素
3. 比较当前遍历的元素和前面的每个元素进行比较，如果比前面的数字小，则进行交换，再和交换后前面的元素进行比较，直到不小于前面的元素或者已经没有元素可以比较，就结束本次排序
4. 重复1,2步骤

评注:
1. 排序结果正确
2. 使用了插入算法实现list从小到大排序

改进:
1. 在append到num_list时可以用int将字符串转化为数字
2. 第五行和第六行的str1和inputa是一样的，所以没必要定义str1，后面直接使用inputa就行

加油
'''