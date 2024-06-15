a=eval(input())
b=[]
for x in a:
    if x==max(a):
        a.remove(x)
    elif x==min(a):
        a.remove(x)
    else:
        b.append(x)
print(b)

