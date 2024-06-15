s=0
m=1
i=0
while m==1:
    a=input()
    if a!='#':
        s+=int(a)
        i+=1
    else:
        m=0
print(i,s)
