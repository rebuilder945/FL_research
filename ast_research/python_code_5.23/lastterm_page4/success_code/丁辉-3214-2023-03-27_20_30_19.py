a1=eval(input())
for i in range(0,len(a1),1):
    if a1[i]==0:
        a2=a1.remove(a1[i])
b=a2+[0]*a1.count(0)
print(b)
