a=eval(input())
l=[]
while len(a)!=0:
    b=max(a)
    l.append(b)
    a.remove(b)
print("".join(str(x) for x in l))







