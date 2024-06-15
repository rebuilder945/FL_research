a=eval(input())
a=[]
for x in range(len(a)):
    a[x]=(a[x]+5)%10

a.reverse()
for i in range(len(a)):
    print(a[i],end='')

    


