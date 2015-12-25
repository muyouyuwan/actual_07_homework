# coding:utf-8

# pzh01.py

def main():
	lst = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
	if len(lst) >= 2 :
		lst.sort(reverse=True)
		print lst[0:2]
	else:
		print u'列表中元素不足2个，无需排序'

if __name__ == '__main__':
	main()
