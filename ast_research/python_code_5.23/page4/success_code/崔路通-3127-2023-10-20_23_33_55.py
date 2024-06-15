a=eval(input())
b=[i+1 for i in range(a)]
c=[b[0]]
print(b)
for i in range(len(b)-1):
    c.append(b[i+1])
print(c)
