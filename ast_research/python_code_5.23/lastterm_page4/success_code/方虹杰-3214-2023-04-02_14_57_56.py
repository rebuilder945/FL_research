a=eval(input())
a1=a.copy()
for x in a:
    if x==0:
        del x
        a.append(0)
print(a1)
    


