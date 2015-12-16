a=[12,3,1,21,2,2,3,4111,22,3333,65534,33,45]
for i in range(1,len(a)):
	temp=a[i]
	p=i-1
	while p>=0 and temp<a[p]:
		a[p+1]=a[p]	
		p-=1
	a[p+1]=temp
print a
