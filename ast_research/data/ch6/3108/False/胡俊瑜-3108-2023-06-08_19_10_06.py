dummy= list(input())
ENG=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',\
     'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',\
     't', 'u', 'v', 'w', 'x', 'y', 'z']
i=0
j=0
k=0
p=0
for x in ENG:
	if dummy.count(x)==0:
		pass
	else:
		print(x,dummy.count(x))
	

