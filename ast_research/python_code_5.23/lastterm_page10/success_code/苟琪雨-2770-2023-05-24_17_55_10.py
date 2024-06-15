a=list(input())
b=list(input())
n=len(a)
f=0
if len(a)==len(b):
    for i in a:
        if i in b:
            b.remove(i)
            f+=1
    if f==n:
        print(True)
    else:
        print(False)
else:
    print(False)
