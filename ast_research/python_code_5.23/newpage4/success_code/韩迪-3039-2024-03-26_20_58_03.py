from re import S


a=list(eval(input()))
b=max(a)
c=min(a)
d=len(a)
S=[]
for i in a:
    if i!=b and i!=c:
        S.append(i)
    else:
        pass

print(S)

