sum=0
n=0
m=1
while(m):
    num=input()
    if num!="#":
        n+=1
        sum+=int(num)
    else:
        m=0
print(n,sum)


