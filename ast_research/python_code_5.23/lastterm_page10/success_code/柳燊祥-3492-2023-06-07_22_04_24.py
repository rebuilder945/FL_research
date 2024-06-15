s=input()
c=[]
for i in s:
    if s.count(i)==1:
        c.append(i)
if c!=[]:
    print(c[0])
else:
    print(None)
