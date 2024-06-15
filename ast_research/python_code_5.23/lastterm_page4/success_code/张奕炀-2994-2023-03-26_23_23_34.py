list1 = eval(input())
n,m = eval(input())
if 0 <= n <= len(list1)-1:
    list2 = [list1[n]]*m
    list1 = list1.extend(list2)
    print(list1)
else:
    print('error')

