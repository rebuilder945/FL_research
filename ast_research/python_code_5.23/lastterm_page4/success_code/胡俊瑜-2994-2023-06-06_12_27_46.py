a=list(eval(input()))
n,m=map(int,input().split(","))
e=[a[n]]*m
print(a+e)
if n>len(a)-1:
	print("error")

