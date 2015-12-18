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