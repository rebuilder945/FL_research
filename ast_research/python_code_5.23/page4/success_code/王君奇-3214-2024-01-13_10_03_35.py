x=eval(input())
for i in x:
    if i==0:
        x.remove(0)
        x.append(0)
print(x)
