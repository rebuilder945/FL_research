a=list(input())
for x in range(len(a)):
    a[x]=(eval(a[x])+5)%10
print(a,end='')


