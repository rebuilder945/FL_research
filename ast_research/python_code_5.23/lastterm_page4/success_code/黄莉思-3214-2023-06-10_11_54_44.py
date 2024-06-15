n=eval(input())
l1=[]
for x in n:
    if x==0:
        l1.append(x)
        n1=n.remove(x)
print(l1+n1)
