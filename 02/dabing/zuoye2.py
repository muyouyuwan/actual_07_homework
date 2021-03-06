#encoding:utf-8

def  inser_sort():
	arr = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
	for i in range(len(arr)):   ##閬嶅巻list
		min_in = i             ##瀹氫箟list涓渶灏忕殑鏁板搴旂殑绱㈠紩
		for j in range(i+1,len(arr)):   ##浠庣i+1涓暟寮€濮嬮亶鍘嗙储寮?
			if arr[min_in] >  arr[j]:   ##濡傛灉鏈€灏忕储寮曞搴旂殑鏁版瘮鍚庨潰鐨勬暟澶э紝閭ｄ箞灏辨妸绱㈠紩鍊艰祴缁欐渶灏忓€肩殑绱㈠紩
				min_in = j
		arr[min_in],arr[i] = arr[i],arr[min_in]               ##绱㈠紩瀵瑰簲鐨勫€间簰鎹綅缃?
	print arr 

inser_sort()


'''
流程:
1. list_1从左到右遍历每一个元素
2. 找到从遍历元素开始到list结束的所有元素中小的与其做交换
3. 重复1, 2步骤

评注:
1. 排序结果正确
2. 定义函数的方式实现功能
3. 使用了选择排序实现list从小到大排序

改进:
1. 如果当前遍历的元素就是从其开始时到list结束位置中最小的，那么就没有比较再做交换(程序优化)
2. 注意文件编码方式, 将文件使用utf-8编码存储, 多人协作必须文件格式统一


num_list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
for i in range(0,len(num_list)):
    min_i = i
    for p in range(i+1, len(num_list)):
        if num_list[min_i] > list[p]:
            min_i = p

    if min_i != i: # 若当前遍历元素不是最小，则将最小元素交换到当前i的位置
        num_list[i], num_list[min_i] = num_list[min_i], num_list[i]

print num_list

'''
