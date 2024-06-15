x,y,z = eval(input())
c = [x]
for i in range(1,y):
    c.append(x+i*z)
print(c)
