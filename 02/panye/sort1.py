d = [7,4,6,4,33,22,890,45,0,4,8,90]

for i in range(1, len(d)):
    tmp = d[i]
    while i > 0 and d[i-1] > tmp:
            #print i
            d[i] = d[i-1]
            i -= 1
            #print d
    d[i] = tmp


print d
