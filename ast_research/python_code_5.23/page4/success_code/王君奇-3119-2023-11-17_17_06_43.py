x=eval(input())
y=[]
for i in range(len(x)):
    if x[i] not in y:
        y.append(x[i])
print(y)
