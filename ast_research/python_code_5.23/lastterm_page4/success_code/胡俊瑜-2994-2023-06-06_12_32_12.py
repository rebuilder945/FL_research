a=list(eval(input()))
n,m=map(int,input().split(","))
if n>len(a)-1:
	print("error")
elif n<=len(a)-1:
	e=[a[n]]*m
	print(a+e)


