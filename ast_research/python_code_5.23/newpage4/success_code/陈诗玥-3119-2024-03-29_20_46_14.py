n=eval(input())
b=[]
for i in range(len(n)-1,-1,-1):
    a=n[i]
    if a in b:
        pass
    else:
        b,insert(0,a)
print(b)
