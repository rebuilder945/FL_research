a=input()
b=input()
c=a
for i in range(len(a)-len(b)+1):
    s=a[i:i+len(b)]
    if s==b:
        c=c.replace(s,' ',-1)
print(c)
