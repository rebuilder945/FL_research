a1=eval(input())
a2=[]
for i in range(len(a1)):
    is_prime=True
    if a1[i]==2:
        a2.append(a1[i])
    else:    
        for j in range(2,(int(a1[i]**0.5)+1)):
            if a1[i]%j==0:
                is_prime=False
                break
        if is_prime==True:
            a2.append(a1[i])
print(a2)
