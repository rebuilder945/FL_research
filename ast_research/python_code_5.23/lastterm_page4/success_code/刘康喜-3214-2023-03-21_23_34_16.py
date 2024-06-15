a=eval(input())
b=a.copy()
c=0
for i in range(0,a.count(0)):
    b.remove(0)
    c=c+1
for j in range(0,c):
    b.append(0)
print(b)
