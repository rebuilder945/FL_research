a=eval(input())
b=[]
for i in range(0,len(a)):
    if a[i].count==1:
        b=b+a[i]
b.sort()
print(b)
