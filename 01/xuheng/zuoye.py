#coding=utf-8
#xh
#作业：LIST最大的2个值
#[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
list_a = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max_1 = 0
max_2 = 0
for i in list_a:
    if i > max_2:
        max_1 = max_2
        max_2 = i
print 'num %s,%s' % (max_1,max_2)

#[1,2,3,2,12,3,1,65543,3,21,2,2,3,11111111,99999,4111,22,3333,444,111,888888,8888,166666,65567,4,5,677,54443,4444,777,68555,45,33,45]
list_b = [1,2,3,2,12,3,1,65543,3,21,2,2,3,11111111,99999,4111,22,3333,444,111,888888,8888,166666,65567,4,5,677,54443,4444,777,68555,45,33,45]
max_a = 0
max_b= 0
for i in list_b:
    if i > max_a :
        if i >max_b:
             max_a = max_b
             max_b = i
        else:
            max_a = i
print 'num %s,%s' % (max_a,max_b)