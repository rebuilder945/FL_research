lis=eval(input())
a=max(lis)
b=min(lis)
while a in lis:
    lis.remove(a)
while b in lis:
    lis.remove(b)
print(lis)
