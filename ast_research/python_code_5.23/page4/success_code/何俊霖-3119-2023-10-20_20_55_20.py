x=eval(input())
y=[]
for i in range(0,len(x)):
    if x[i] not in y:
        y.append(x[i])
    else:
        continue
print(y)

