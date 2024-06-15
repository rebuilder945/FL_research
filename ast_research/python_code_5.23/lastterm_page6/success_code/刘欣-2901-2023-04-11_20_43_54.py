m=1
sum=0
n=0
while(m):
    s=input()
    if s!="#":
        n+=1
        sum+=int(s)
    else:
        m=0
        print("%d"%n,sum)
