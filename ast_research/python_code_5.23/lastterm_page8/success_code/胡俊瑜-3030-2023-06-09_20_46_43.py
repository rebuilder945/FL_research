a0=input().split(",")
b0=input().split(",")
b0_1=[]
c0=len(a0)
for x in b0:
    az=int(x)
    b0_1.append(az)
d={}
for x in range(c0):
    d[a0[x]]=b0_1[x]
a=[]
for k,v in d.items():
		s=f"{k}{v}"
		s2=[]
		s.split()
		b=s[1]
		b=int(b)
		c=s[0]
		s2.append(c)
		s2.append(b)
		a.append(s2)
print(a)

   

