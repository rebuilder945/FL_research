a=eval(input())
b=[]
for i in range(a):
    b.append(i)
for i in range(len(b)-1):
    b[i]=b[i+1]
print(b)
