#encoding: utf-8
num_list = [4, 3, 2, 1, 5]
for i in range(1, len(num_list)):
    print '对索引%d元素%s进行排序' % (i, num_list[i])
    for idx in range(i, 0, -1):
        if num_list[idx] < num_list[idx - 1]:
            num_list[idx], num_list[idx - 1] = num_list[idx - 1], num_list[idx]
        else:
            break
    print '排序完成:%s\n' % num_list
            
print '最终:%s' % num_list
