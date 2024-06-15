a=int(input())
n1=[]
n2=[]
for x in a:
    for i in range(2,x):
        if a%i==0:
            n1.append(i)
        else:
            n2.append(i)
print(n2)
