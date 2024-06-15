a=list(eval(input()))
b,c=eval(input())
f=len(a)
d=[]
if b>f:
	print('error')
else:
	d.append(a[b])
	d=d*c
	e=a+d
	print(e)




