#!/usr/bin/env python
#encoding:utf8
print '''
        nginx 访问数量前十的ip:
'''
read_log = open('/root/access.log','r')
dict_log = {}
list_log = []


for log_line in read_log:
    ip =  log_line.split()[0]
    url =  log_line.split()[6]
    status =  log_line.split()[8]
    dict_log.setdefault((ip,url,status),0)
    dict_log[(ip,url,status)] += 1
for s,y in dict_log.items():
     list_log.append((s[0],s[1],s[2],y))
######
print '''one::::

'''
if len(list_log) > 10:
   sort =10
for ch in range(sort):
    for x in range(len(list_log) -1,0,-1):
        if (list_log[x])[3] > (list_log[x - 1])[3]:
            list_log[x],list_log[x - 1] = list_log[x - 1],list_log[x]
        elif (list_log[x])[0] == (list_log[x - 1])[0]:
            list_log[x],list_log[x - 1] = list_log[x - 1],list_log[x]
        else:
            continue
    list_log2 = list_log[:ch + 1]
for ii in  list_log2:
    print ii

print '''two::::老师有机会可不可以讲解一下排序lambda的用法，这是网上搜索的

'''
list_log.sort(key=lambda x:x[3],reverse=True)
for i in list_log[:10]:
    print i
