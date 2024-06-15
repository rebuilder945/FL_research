ls=eval(input())
ls1=ls.copy()
for i in range(len(ls)):
	a=ls.count(ls(i))
	if a>1:
		for b in range(a-1):
			ls1.remove(ls(i))
	else:
			continue
print(ls1)
			
