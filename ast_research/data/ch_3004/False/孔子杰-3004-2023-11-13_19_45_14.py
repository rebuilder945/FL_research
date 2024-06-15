lst=eval(input())
a=[]
for x in lst:
    if x>=2:
        for i in range(2,x,1):
            x%i==0
            break
        else:
            a.append(x)
print(a)

