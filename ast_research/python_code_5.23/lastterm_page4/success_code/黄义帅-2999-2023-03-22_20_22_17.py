A=input().split('')
n,m=input().split('')
list=list(A)
n=int(n)
m=int(m)
list[n],list[m]=list[m],list[n]
print(list)
