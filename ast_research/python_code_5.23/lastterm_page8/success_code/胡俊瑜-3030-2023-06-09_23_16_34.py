a0=input().split(",")
b0=input().split(",")
d={}
for x in range(len(a0)):
	c=a0[x]
	d[c]=b0[x]
a=[]
for k,v in d.items():
	a.append([k,int(v)])
a.sort(key=lambda x:x[1])
print(a)

   

