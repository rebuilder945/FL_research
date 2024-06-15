a=eval(input())
b=[]
for i in a:
    if i!=0:
        b.append(i)
n=a.count(0)
for i in range(n):
    b.append(0)
print(b)
