a=eval(input())
c=a.sort(Reverse=False)
b=[]
for x in c:
    if x not in b:
        b.append(x)
print(b)

