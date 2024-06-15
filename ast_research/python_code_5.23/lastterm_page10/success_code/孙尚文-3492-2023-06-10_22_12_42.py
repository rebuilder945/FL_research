a=input()
c=[]
b=[]
for i in a:
    c.append(i)
for i in c:
    if c.count(i)==1:
        b.append(i)
if b==[]:
    print("None")
else:
    print(b[0])

