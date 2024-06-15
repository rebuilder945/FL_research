a=eval(input())
b=a.count(max(a))
c=a.count(min(a))
for i in range(1,b+1):
    a.remove(max(a))
    a.remove(min(a))
print(a)

