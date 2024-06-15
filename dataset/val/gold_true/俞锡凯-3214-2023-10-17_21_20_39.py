a=eval(input())
c=a.count(0)
for i in range(c):
    a.remove(0)
for i in range(c):
    a.append(0)
print(a)

        
