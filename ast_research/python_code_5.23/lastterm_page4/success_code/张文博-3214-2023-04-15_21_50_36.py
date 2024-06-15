m=eval(input())
j=0
n=m
for i in m:
    if i==0:
        n.remove(0)
        j=j+1
for x in range(j):
    n.append(0)   
print(n)
