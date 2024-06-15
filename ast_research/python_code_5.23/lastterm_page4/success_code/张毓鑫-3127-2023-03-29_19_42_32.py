a=eval(input())
b=[]
for i in range(a):
    b.append(i)
for i in len(b)-1:
    b[i]=b[i+1]
print(b)
