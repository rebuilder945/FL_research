x=eval(input())
lis=[]
for a in x:
    if a==2:
        lis.append(a)
    else:
        for b in range(2,a//2+2):
            if  a%b==0:
                break
            elif b==a//2+1:
                lis.append(a)
print(lis)
