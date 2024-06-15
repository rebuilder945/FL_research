a=eval(input())
ma=max(a)
mi=min(a)
b=[]
for i in a:
    if i!=ma and i!=mi:
        b.append(i)
print(b)
