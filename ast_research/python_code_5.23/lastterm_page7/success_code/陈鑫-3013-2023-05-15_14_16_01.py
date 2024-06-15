a=input()
b=[]
c=[]
while a!="ok":
    d = a.split()
    b.append(d[0])
    c.append(d[-1])
    a=input()
c.sort()
print(b)
print(c)
if "india" in b:
    print("yes")
else:
    print('no')
c=list(map(int,c))
print(sum(c))
