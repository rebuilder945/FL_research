n=list(input())
m=0
x=0
for i in n:
    a=(eval(i)+5)%10
    b=a*10**x
    x+=1
    m+=b
print(m)
