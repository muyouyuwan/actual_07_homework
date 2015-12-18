list1 = [1, 2, 3, 2, 12, 3, 1, 3, 21, 2, 2, 3, 4111,
         22, 3333, 444, 111, 4, 5, 777, 65555, 45, 33, 45]
for i in range(1, len(list1)):
    for j in xrange(0, i):
        if list1[i] < list1[j]:
            list1[i], list1[j] = list1[j], list1[i]

print list1
