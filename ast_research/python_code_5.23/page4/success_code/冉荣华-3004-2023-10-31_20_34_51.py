n=input().split(',')
c=[]
for i in n:
    if int(i)>=2:
        for x in range(2,i,1):
            if i%x==0:
                break
            else:
                c.append(i)
print(c)


