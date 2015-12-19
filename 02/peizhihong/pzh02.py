# coding:utf-8

# pzh02.py-插入排序

def charuSort(lst):
	nloops = len(lst)
	for i in range(1, nloops):
		for j in range(i, 0, -1):
			if lst[j-1] > lst[j]:
				lst[j-1], lst[j] = lst[j], lst[j-1]
			else:
				break
	return lst

def main():
	lst = [5, 6, 3, 1, 8, 7, 2, 4]
	ordLst = charuSort(lst)
	print ordLst

if __name__ == '__main__':
	main()
