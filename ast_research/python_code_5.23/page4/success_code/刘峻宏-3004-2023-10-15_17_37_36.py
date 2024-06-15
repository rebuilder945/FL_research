a=eval(input())
i=0
b=[]
for i in range(len(a)):
    n=a[i]
    for x in range (n):
        if not n%x==0:
            break
        else:
            pass
    i+=1
    b.append(n)
print(b)
