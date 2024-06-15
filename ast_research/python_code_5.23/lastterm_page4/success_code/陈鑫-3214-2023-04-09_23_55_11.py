a=eval(input())
b=[]
for i in range(len(a)):
    if a[i]==0:
        a.pop(i)
        a.append(0)
print(a)
