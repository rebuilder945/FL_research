a=eval(input())
b=max(a)
c=min(a)
d=a.copy()
i=0
while i<len(a):
    for x in d:
        if x==b or x==c:
            d.remove(x)
    i+=1
print(d)
