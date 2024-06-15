m=eval(input())
n=[]
a=min(m)
b=max(m)
ls=[a,b]
for i in m:
    if i not in ls:
        n.append(i)
    else:
        pass
print(n)
