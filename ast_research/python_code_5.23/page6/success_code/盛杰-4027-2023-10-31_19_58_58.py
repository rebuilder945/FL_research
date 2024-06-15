lst=[]
for i in range(10000):
    n=input()
    if n=="#":
        break
    else:
        lst.append(int(n))
s=sum(lst)
l=len(lst)
print(l,s)
