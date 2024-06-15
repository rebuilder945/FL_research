ls=eval(input())
a=[]
for x in range(len(ls)):
    b=ls[x]
    if b in ls[x+1:]:
        continue
    else:
        a.append(b)
print(a)
