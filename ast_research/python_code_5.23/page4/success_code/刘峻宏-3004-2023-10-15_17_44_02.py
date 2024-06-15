a=eval(input())
i=0
b=[]
for i in range(len(a)):
    n=a[i]
    for x in range (n):
        y=x+1
        if not n%y==0:
            break
        else:
            pass
    i+=1
    b.append(n)
print(b)
