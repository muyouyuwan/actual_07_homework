list_1 = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
list_2 = []
for i in range(len(list_1)):
    list_2.append(list_1[i])
    for j in range(len(list_2)-1,0,-1):
        if list_2[j] < list_2[j-1]:
            list_2[j],list_2[j-1] = list_2[j-1],list_2[j]
        else:
            break
print list_2
