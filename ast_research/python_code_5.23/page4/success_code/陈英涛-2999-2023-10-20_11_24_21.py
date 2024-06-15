list1 = list(map(str,input().split()))
n,m = map(int,input().split())
list1[n],list1[m] = list1[m],list1[n]
print(list1)


