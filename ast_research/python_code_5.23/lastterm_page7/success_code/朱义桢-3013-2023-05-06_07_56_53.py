n={}
while True:
    a=input()
    if a=="ok":
        break
    k,v=a.split()
    n[k]=int(v)
m=sorted(n.keys())
print(m)
b=sorted(n.values())
print(b)
if "India" in n:
    print("yes")
else:
    print("no")
print(sum(b))

