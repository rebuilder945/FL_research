a=eval(input())
n,m=input()
if n<=m and m<=len(a):
	b=del a[n:m]
	print(b)
else:
	print("Error")

