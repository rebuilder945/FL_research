A=input().split(' ')
n,m=int(input().split(' '))
lst=list(A)
lst[n],lst[m]=lst[m],lst[n]
print(lst)
