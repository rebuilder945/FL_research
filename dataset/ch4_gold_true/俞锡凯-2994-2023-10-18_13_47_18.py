a=list(eval(input()))
n,m=eval(input())
c=len(a)
d=[]
if n>c:
    print("error")
else:
    for x in range(m):
         d.append(a[n])
    a=a+d
    print(a)

        
    


