a=input()
b=input()
f=1
while f==1:
    f=0
    if b in a:
        a=a.replace(b,'')
        f=1
print(a)
