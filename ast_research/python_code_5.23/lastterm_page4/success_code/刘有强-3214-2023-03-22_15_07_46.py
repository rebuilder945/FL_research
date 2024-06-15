from os import remove

lst=eval(input())
lst1=lst.copy()
for x in lst1:
	if x==0:
		lst.remove(x)
		lst.append(0)
print(lst)
