a=int(eval(input()))
b=[]
for i in range(a+1):
    b.append(i)
b.remove(0)
b.remove(1)
b.append(1)
print(b)
