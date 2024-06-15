n=eval(input())
l=[x for x in range(1,n+1)]
for i in range(1):
    num=l.pop(0)
    l.append(num)
print(l)
