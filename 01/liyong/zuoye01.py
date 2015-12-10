list1 = [1, 2, 3, 2, 12, 3, 1, 3, 21, 2, 2, 3, 4111,22, 3333, 444, 111, 4, 5, 777, 65555, 45, 33, 45]
max1 = 0
max2 = 0
for num1 in list1:
    if max1 < num1:
        max1 = num1
    for num2 in list1:
        if max2 < num2 and num2 < max1:
            max2 = num2
print 'max1 : %s' % max1
print 'max2 : %d' % max2
