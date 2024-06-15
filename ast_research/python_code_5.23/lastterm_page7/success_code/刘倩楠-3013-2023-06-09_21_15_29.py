n=input()
a=[]
b=[]
while n!="ok":
    key,value=n.split(" ")
    a.append(key)
    b.append(value)
    n=input()
lb=list(map(int,b))
print(a)
print(lb)
if "India" in a:
    print("yes")
else:
    print("no")
print(sum(lb))
