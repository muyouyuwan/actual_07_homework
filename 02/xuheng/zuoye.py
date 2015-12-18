#coding=utf-8
seq = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

for i in range(1,len(seq)):
        tmp=seq[i]
        pos=i;
        for j in range(i-1,-1,-1):
            if seq[j]>tmp:
                seq[j+1]=seq[j]
                pos=j
            else:
                break
        seq[pos]=tmp
       # print '排序分解:%s' %seq
print '排序结果:%s' %seq #排序结果




