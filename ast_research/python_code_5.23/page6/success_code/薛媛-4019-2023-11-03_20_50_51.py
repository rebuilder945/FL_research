a=input()
e=[]
for x in range(len(a)):
    e.append((int(a[x])+5)%10)
c=e.copy()
for i in range(len(a)):
        c[i]=e[len(a)-i-1]
        d=''.join(str(i)for i in c)
print(d)


    
