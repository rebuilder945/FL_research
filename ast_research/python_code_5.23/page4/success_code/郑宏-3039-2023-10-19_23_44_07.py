ls=eval(input())
a=max(ls)
a1=ls.count(a)
b=min(ls)
if a==b:
	ls=[]
else:
    b1=ls.count(b)
    for i in range(a1):
	    ls.remove(a)
    for x in range(b1):
	    ls.remove(b)
print(ls)
