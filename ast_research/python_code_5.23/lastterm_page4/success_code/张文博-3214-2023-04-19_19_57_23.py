m=eval(input())
j=0
for i in m:
    if i==0:
        j=j+1
for x in range(j):
    m.remove(0)
    m.append(0)   
print(m)

