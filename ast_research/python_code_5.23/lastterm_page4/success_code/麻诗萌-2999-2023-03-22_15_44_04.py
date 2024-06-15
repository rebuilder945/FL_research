import copy
lst=input().split()
n,m=map(int,input().split())
lst0=lst.deepcopy()
lst0[n]=lst[m]
lst0[m]=lst[n]
print(lst0)


