a=eval(input())
for i in range(len(a)):
	b=max(a)
	a.remove(b)
	if sum(a)==0:
		print(0)
		break
	else:
		print(b,end='')






