a=list(input())
b=list(input())
a.sort()
b.sort()
f=True
if len(a)!=len(b):
    f=False
else:
    for i in range(len(a)):
        if a[i]!=b[i]:
            f=False
print(f)

