a=input().split()
b=input().split()
a=list(a)
b=list(b)
a=a.sort()
b=b.sort()
a=set(a)
b=set(b)
if a==b:
    print("True")
else:
    print("False")
