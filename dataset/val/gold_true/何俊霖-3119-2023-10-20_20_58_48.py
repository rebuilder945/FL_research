x=eval(input())
y=[]
for i in range(-1,-len(x),-1):
    if x[i] not in y:
        y.insert(0,x[i])
    else:
        continue
print(y)

