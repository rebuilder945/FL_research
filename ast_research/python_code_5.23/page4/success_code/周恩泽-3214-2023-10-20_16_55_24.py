n1=eval(input())
n2=[]
for x in n1:
    if x==0:
        n2.append(x)
while 0 in n1:
    n1.remove(0)
for x in range(len(n2)):
    n1.append(0)
print(n1)

