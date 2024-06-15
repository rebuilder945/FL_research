a=eval(input())
for i in a:
	for  x in range(2,i):
					if i==1 or i==0:
						a.remove(i)
						break
					elif i%x==0:
						a.remove(i)
						break
print(a)
					
