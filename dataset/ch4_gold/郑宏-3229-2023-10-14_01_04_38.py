a=eval(input())
b=[]
for i in range(len(a)):
	c=a.count(a[i])
	if c==1:
		b.append(a[i])
b=list(set(b))
if b==[]:
		print('error')
else:
		for i in range(len(b)-1):
		    print(b[i],end=',')
		print(b[-1])

		
		

