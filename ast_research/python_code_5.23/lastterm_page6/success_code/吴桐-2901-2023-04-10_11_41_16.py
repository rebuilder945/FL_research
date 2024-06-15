sums=0
n=0
m=1
while(m):
    s=input()
    if (s!="#"):
        n+=1
        sum+=int(eval(s))
    else:
        m=0
print(n,sums)
