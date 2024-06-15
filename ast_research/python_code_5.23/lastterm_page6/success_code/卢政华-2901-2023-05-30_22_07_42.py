sum=0
a=0
m=0
while m==0:
    s=eval(input())
    if s !="#":
        a+=1
        sum+=int(s)
    else:
        m=0
print(sum,a)

