a=input().split()
b=[]
c=[]
while a!="ok":
    b.append(a[0])
    c.append(a[1])
b.sort()
c.sort()
print(b)
print(c)
if "india" in b:
    print("yes")
else:
    print('no')
c=list(map(int,c))
print(sum(c))
