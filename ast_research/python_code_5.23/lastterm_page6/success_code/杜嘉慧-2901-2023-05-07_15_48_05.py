s=input()
sums=0
n=0
m=1
while(m):
    if s!="#":
        sums+=int(s)
        n+=1
    else:
        m=0
print(n,sums)
