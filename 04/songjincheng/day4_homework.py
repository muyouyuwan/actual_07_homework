#!/usr/bin/env python
#-*- coding:utf-8 -*-

#status, url, ip
#['404', '/images/cursor zoom.cur', ('118.112.143.148', 674)]
dic = {}
dic_list = []
f = open('www_access_20140823.log','r+')
for i in f.read().split('\n'):
    logfile = i.split()
    status = logfile[8]
    url = logfile[6]
    ip = logfile[0]
    dic[ip] = dic.setdefault(ip,1) + 1
    for ip,count in dic.items():
        dic_list.append([status,url,(ip,count,)])
    for i in sorted(dic_list, key=lambda cmp:cmp[2][1],reverse=True)[0:10]:
        print i 

      
    

    
