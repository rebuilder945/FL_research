a=eval(input())
l=[]
while len(a)!=0:
    b=max(a)
    l.append(b)
    a.remove(b)
if l.count(0)==len(l):
    for i in range(len(l)-1):
        l.remove(0)
print("".join(str(x) for x in l))







