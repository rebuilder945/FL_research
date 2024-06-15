m=eval(input())
n=set(m)
l=sorted(m)
for x in n:
    l.remove(x)
l=set(l)
a=list(n-l)
a.sort()
if a==[]:
    print("False")
else:
    print(",".join(str(i) for i in a))


        







