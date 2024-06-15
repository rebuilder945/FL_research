s=input()
s=list(s)
c=[]
for x in s:
   if s.count(x)==1:
    c.append(x)
if c==[]:
    print("None")
else:
    print(c[0]) 
