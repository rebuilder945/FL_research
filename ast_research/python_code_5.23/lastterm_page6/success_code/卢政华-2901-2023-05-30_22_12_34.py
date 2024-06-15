sums=0
a=0
m=0
while m==0:
    s=eval(input())
    if s !="#":
        a+=1
        sums+=int(s)
    else:
        m=1
print(sums,a)

