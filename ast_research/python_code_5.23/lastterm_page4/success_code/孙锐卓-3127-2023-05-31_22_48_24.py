a=eval(input())
x=[x for x in range(1,a+1)]
print(x)
for i in range(a-1):
    x[i],x[i+1]=x[i+1],x[i]
print(x)











