a=input()
n1=[]
n2=[]
for i in a:
    for x in range(2,i):
        if i%x==0:
            n1.append(i)
        else:
            n2.append(i)
print(n2)
