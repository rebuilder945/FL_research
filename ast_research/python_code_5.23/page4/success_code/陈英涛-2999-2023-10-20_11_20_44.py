list1 = list(map(str,input().split()))
n,m = eval(input())
list1[n],list1[m] = list1[m],list1[n]
print(list1)


