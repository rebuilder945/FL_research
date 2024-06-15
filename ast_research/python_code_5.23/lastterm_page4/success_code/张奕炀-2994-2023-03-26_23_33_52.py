list1 = input().split(',')
n,m = eval(input())
if -len(list1) <=  n <= len(list1)-1:
    list2 = [list1[n]]*m
    list1 = list1 + list2
    list1 = [int(x) for x in list1]             #将列表中的所有元素的类型从字符串转为整型
    print(list1)
else:
    print('error')

