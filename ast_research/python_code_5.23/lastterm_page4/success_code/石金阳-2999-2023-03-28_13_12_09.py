A=input().split(' ')
n,m=input().split(' ')
lst=list(A)
n=int(n)
m=int(m)
lst[n],lst[m]=lst[m],lst[n]	#交换列表元素位置
print(lst)

