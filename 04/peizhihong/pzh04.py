# coding:utf-8

# pzh04.py

from collections import Counter

infoLst = []
resLst = []

with open('www_access_20140823.log', 'r') as f:
	content = f.xreadlines()
	for line in content:
		line = line.strip()
		info = line.split('\\', 1)[0].strip()
		ip = info.split(' ', 1)[0]
		status = info.split(' ')[-1]
		url = info.split('"', 2)[1].split(' ')[1]
		infoLst.append((ip,status,url))

resDict = Counter(infoLst)

for key, value in resDict.items():
	resLst.append([key[1], key[2], (key[0], value)]) 

for i in resLst:
	print i


