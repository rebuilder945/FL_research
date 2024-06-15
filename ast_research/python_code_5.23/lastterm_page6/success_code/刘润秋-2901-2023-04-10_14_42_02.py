sum=0
n=0
m=1
while(m==1):
    s=input()
    if (s!="#"):
        n+=1
        sum+=int(s)
    else:
        m=0
print(n,sum)

