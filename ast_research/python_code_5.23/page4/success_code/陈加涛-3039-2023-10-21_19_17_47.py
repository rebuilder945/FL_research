a=eval(input())
b=a.count(max(a))
c=a.count(min(a))
if len(a)>1:
    for i in range(1,b+1):
        a.remove(max(a))
    if len(a)!=0:
        for i in range(1,c+1):
            a.remove(min(a))
print(a)

