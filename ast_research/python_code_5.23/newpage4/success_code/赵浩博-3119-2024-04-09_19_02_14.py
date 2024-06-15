a=eval(input())
a2=[]
for i in range(len(a)):
    if a[i:].count(a[i])==1:
        a2.append(a[i])
print(a2)
