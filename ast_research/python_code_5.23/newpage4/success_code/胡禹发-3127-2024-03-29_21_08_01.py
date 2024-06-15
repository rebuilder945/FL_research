n=eval(input())
b=[]
for i in range (n):
    b.append(i)
b.remove(0)
b.append(n)
b.remove(1)
b.append(1)
print(b)
