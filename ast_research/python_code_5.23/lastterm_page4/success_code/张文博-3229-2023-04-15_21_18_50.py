m=eval(input())
n=set(m)
l=sorted(m)
for x in n:
    l.remove(x)
l=set(l)
a=n-l
print(list(a))


        







