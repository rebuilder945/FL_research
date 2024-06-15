x=eval(input)
y=list(x)
z=[]
z.append(y[0])
for i in range(y[1]):
    m =y[0]+ i*y[2]
    z.append(m)
print(z)
