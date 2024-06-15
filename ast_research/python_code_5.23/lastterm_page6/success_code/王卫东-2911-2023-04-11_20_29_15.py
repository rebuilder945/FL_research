a = list(input())
for x in range(len(a)):
    a[x]=(int(a[x])+5)%10
a[0],a[-1]=a[-1],a[0]
a[1],a[-2]=a[-2],a[1] 
b = "".join(map(str,a))
print(b)   
