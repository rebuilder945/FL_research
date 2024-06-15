a=eval(input())
n=a.count(0)
b=list(set(a))
b.sort(key=a.index)      
b.remove(0)
for i in range(n):
    b.append(0)
print(b)

