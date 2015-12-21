list1 = [11,43,4,57,888,99768,245,333,4433]
for i in range(1, len(list1)):
    for j in range(i, 0, -1):
        if list1[j] < list1[j - 1]:
            list1[j], list1[j - 1] = list1[j - 1], list1[j]
        else:
            break
print list1
