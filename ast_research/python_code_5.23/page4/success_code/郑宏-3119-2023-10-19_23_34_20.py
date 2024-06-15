ls=eval(input())
ls1 =ls[:]
for i in range(len(ls)):
	a=ls1.count(ls[i])
	if a>1:
			ls1.remove(ls[i])
	else:
		continue
print(ls1)
