n=input()
a=[]
b=[]
while n!="ok":
    k,v=n.split(" ")
    a.append(k)
    b.append(v)
    n=input()
a.sort()
b.sort()
lb=list(map(int,b))
print(a)
print(lb)
if "India" in a:
    print("yse")
else:
    print("no")
print(sum(lb))
