a=eval(input())
d=[]
for x in a:
	if a.count(x)==1:
	    d.append(x)     
e=sorted(d)
if d!=[]:
	print(",".join('%s'%id for id in e)) #字符串占位符
else:
	print(False)
		

