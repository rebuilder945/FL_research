n1=eval(input())
n2=[]
for i in range(len(n1)):
    a=n1[i]
    if a==1:
        continue
    for x in range(2,a):
        if a%x==0:
            break
    else:
        n2.append(a)
print(n2)
