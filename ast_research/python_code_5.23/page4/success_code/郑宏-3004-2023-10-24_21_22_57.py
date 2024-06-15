a=eval(input())
for i in a:
	for  x in range(2,int(i/2)):
			if i%x==0:
				a.remove(i)
			
print(a)
			
