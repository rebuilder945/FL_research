x=eval(input())
y=[]
for i in range(0,len(x)):
    if x[i]==0:
        y.append(x[i])
for n in range(1,len(y)+1):
    x.remove(0)
e=x+y
print(e)
