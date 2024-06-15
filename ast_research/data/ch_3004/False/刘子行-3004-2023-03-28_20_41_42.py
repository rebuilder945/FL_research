shit=eval(input())
fuck=[]
ass=[]
for x in shit:
    for i in range(2,x):
        if x%i==0:
            fuck.append(x)
for x in shit:
    if x not in fuck:
        ass.append(x)
print(ass)
