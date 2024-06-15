a = eval(input())
b=max(a)
c=min(a)
d=[]
for x in a:
    if x>c and x<b:
        d.append(x)
print(d)






