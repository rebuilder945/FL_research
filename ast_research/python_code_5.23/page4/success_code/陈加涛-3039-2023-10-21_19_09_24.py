a=eval(input())
b=a.count(max(a))
c=a.count(min(a))
if len(a)>1:
    for i in range(1,b):
        a.remove(max(a))
        a.remove(min(a))
print(a)

