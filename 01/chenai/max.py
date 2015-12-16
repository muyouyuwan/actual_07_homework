shuzu = [1,2,3,2,12,23,2,3,2,4111,22,222,3333,444,111,4,5,777,65555,45,33,45]
max1 = 0
max2 = 0
for i in shuzu:
    if i > max1:
        max1 = i
        for j in shuzu:
            if j < max1 and j > max2:
               max2 = j

print 'max1 is %s , max2 is %s' %(max1,max2)
