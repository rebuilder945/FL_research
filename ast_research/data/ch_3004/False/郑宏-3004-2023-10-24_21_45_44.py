a=eval(input())
for i in a:
	for  x in range(2,int(i)):
			if i%x==0 or i==0 or i==1:
				a.remove(i)
				break
			else:
				continue
print(a)
					
