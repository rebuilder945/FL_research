a1=eval(input())
b=[]
for i in range(0,len(a1),1):
        if a1[i]!=0:
                b.append(a1[i])
c=b+[0]*a1.count(0)
print(c)
