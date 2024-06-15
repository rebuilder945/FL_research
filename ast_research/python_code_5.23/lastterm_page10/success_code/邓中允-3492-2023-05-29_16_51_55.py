s=input()
a=[]
c=str(s)
if s=="":
    print("None")
else:
    for i in range(len(c)):
        if c.count(i)==1:
            a.append(c[i])
print(a[0])

