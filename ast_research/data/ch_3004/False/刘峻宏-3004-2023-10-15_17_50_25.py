a=eval(input())
i=0
b=[]
for i in range(len(a)):
    n=a[i]
    for x in range (n):
        y=x+1
        if n%y==0:
            pass
        else:
            continue
    i+=1
    b.append(n)
print(b)
