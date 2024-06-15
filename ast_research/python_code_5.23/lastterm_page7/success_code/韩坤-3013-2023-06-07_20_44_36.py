dic={}
lst1=[]
lst2=[]
while True:
    n=input()
    if n=="ok":
        break
    else:
        a,b=n.split()
        dic[a]=int(b)
        lst2.append(int(b))
        lst1.append(a)
        x=sum(lst2)
print(sorted(lst1))
print(sorted(lst2))
if "India" in dic:
        print("yes")
else:
        print("no")
print(x)
