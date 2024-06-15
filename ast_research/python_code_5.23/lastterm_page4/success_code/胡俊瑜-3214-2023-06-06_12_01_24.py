a=eval(input())
c=[]
for x in a:
	idx=a.index(x)
	if x==0:
		e=a.pop(idx)
		c.append(e)
print(a+c)

