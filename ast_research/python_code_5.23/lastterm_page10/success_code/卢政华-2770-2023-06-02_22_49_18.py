a=input().split()
b=input().split()
a=list(a)
b=list(b)
a=a.sort()
b=b.sort()
if set(a) == set(b):
    print("True")
else:
    print("False")
