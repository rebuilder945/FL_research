lst=input().split()

n,m=map(int, input().split())

lst[m],lst[n]=lst[n],lst[m]
print(lst)
