a=list(input())
for i in range(len(a)):
    a[i]=(eval(a[i])+5)%10
a[0],a[-1],a[1],a[-2]=a[-1],a[0],a[-2],a[1]
for x in a:
    print(x,end="")

