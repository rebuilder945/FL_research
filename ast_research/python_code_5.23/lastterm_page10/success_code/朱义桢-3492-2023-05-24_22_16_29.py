a=input()
a=" ".join(a)
a=a.split()
b=[]
for x in a[:]:
    if a.count(x)==1:
        b.append(x)
if b==[]:
    print("None")
else:
    print(b[0])
