a=eval(input())
n=a.count(max(a))
m=a.count(min(a))
for i in range(n):
    a.remove(max(a))
for i in range(m):
    a.remove(min(a))

    

print(a)
    







             
