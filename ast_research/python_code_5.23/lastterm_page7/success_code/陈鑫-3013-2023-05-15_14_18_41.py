a=input()
b=[]
c=[]
while a!="ok":
    d = a.split()
    b.append(d[0])
    c.append(d[-1])
    a=input()
b.sort()
c=list(map(int,c))
c.sort()
print(b)
print(c)
if "ndia" in b:
    print("yes")
else:
    print('no')

print(sum(c))
