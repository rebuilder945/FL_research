ls1=input().split()
s=input()
ls2=s.split()
a=int(ls2[0])
b=int(ls2[1])
if ls1[a]==ls1[b]:
	print(ls1)
elif a>b:
	c=ls1.pop(a)
	d=ls1.pop(b)
	ls1.insert(b,c)
	ls1.insert(a,d)
	print(ls1)
else:
    c=ls1.pop(a)
    d=ls1.pop(b-1)
    ls1.insert(a,d)
    ls1.insert(b,c)
    print(ls1)

