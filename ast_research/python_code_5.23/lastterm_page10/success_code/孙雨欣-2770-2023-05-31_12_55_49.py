a=list(input())
b=list(input())
a.sort()
b.sort()
f=True
if len(a)!=len(b):
    f=False
else:    
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]!=b[j]:
                f=False
print(f)

