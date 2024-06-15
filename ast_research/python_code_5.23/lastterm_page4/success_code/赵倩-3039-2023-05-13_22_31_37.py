a = eval(input())
b=max(a)
c=min(a)
for x in a:
    if x==b:
        a.remove(x)
        
    elif x==c:
        a.remove(x)
print(a)






