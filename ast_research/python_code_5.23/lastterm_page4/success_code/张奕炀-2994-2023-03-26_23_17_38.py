list1 = eval(input())
n,m = eval(input())
if 0 <= n <= len(list1)-1:
    list2 = [list1[n]]*m
    list1 = list1 + list2
    print(list1)
elif -len(list1) <= n < 0:
    list2 = [list[n]]*m
    list1 = list1 + list2
else:
    print('error')

