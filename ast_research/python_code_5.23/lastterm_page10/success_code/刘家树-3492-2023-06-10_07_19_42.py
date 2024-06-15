a=input() or "None"
if a=="None":
    print("None")
l=list(a)
b=[]
for x in l:
    c=l.count(x)
    if c==1:
        b.append(x)
print(b[0])


