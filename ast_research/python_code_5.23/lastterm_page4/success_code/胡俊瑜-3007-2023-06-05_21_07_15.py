a=eval(input())
n,m=input()
if n<=m and m<=len(a):
	b=a.pop(n,m)
	print(b)
else:
	print("Error")

