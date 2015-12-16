max1=0
max2=0
a=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
for i in a:
	if max1<i:
		max1=i
for j in a:
	if j==max1:
		continue
	elif max2<j:
		 max2=j
print max1
print max2