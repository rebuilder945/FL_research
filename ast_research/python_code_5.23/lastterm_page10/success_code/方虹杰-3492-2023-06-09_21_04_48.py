a=input()
b=list(a)
c=[]
for i in b:
    if b.count(i)==1:
        c.append(i)
if c==[]:
    print("None")
else:
    print(c[0])

