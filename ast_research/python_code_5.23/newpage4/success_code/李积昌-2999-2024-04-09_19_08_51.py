a=list(input().split())
b,c=input().split()
b=eval(b)
c=eval(c)
d=a[b]
e=a[c]

a[b]=e
a[c]=d
print(a)

        
