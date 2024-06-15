a=eval(input())
b=[]
for i in range(a):
    if i!=0:
        b.append(i)
for i in range(1):
    b.insert(len(b),b[0])
    b.remove(b[0])
print(b)
