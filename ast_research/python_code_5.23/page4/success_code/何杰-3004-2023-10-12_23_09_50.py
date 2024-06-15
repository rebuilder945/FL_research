n1=eval(input())
n2=[]
i=0
while i<len(n1):
    a=n1[i]
    i+=1
    for x in range(2,a):
        if a%x==0 or a==1:
            break
    else:
        n2.append(a)
print(n2)
