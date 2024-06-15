n=input()
a=""
for x in n:
    x=(int(x)+5)%10
    a+=str(x)
a=list(a)
a.reverse()
b=""
for x in a:
    b+=a
print(b)
print(type(a))


