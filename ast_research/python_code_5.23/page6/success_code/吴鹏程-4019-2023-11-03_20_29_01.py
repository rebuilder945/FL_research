a=eval(input())
c=[]
for x in range(len(a)):
    c[x]=(a[x]+5)%10
a.reverse()
for i in range(len(a)):
    print(c[i],end='')

    


