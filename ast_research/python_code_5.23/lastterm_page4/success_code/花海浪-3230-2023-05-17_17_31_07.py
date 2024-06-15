a=eval(input())
a.sort(reverse=True)
print(a)
c=len(a)-1
d=0
for i in a:
    d+=i*(10**c)
    c=c-1
print(d)


