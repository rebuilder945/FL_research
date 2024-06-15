list1 = input().split(',')
n,m = eval(input())
if 0 <= n <= len(list1)-1:
    list2 = [list1[n]]*m
    list1 = list1 + list2
    for i in list1:
        list1[i] = int(list1[i])
    print(list1)
else:
    print('error')

