#coding:utf-8
f = open('www_access_20140823.log', 'r')
# f = open('1.log', 'r')
_dir = {}
_list = [] 
# 1、统计访问次数（注意同一个IP，可能访问不同的url以及htpp状态） 
##定义字典_dir{(访问状态，访问http，访问IP)，访问次数}
for _line in f.readlines():
	access_ip = _line.split()[0]
	access_state = _line.split()[8]
	access_url = _line.split()[6]
	tmp_list = [access_state,access_url,access_ip]
	_key = tuple(tmp_list)
	_dir.setdefault(_key,1)
	if tmp_list in _list:
		_dir[_key] += 1
	else:
		_list.append(tmp_list)
#2、根据题意，输出结果
a_list = []
for i in _dir.items():
	list1 = [i[0][0],i[0][1],tuple([i[0][2],i[1]])]
	a_list.append(list1)
#3、根据访问次数，排序
for j in range(len(a_list)-1):
	for i in range(len(a_list)-1-j):
		if a_list[i][2][1] < a_list[i+1][2][1]:
			a_list[i],a_list[i+1] = a_list[i+1],a_list[i]
print a_list[:10]