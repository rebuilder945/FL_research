a=eval(input())
b=max(a)
c=min(a)
s1=(b,c)
d=[]
for i in a: 
	if i not in s1:
	    d.append(i) 
print(d)
 

