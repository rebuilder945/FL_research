n,m=input().split(" ")
n=int(n)
m=int(m)
s=[]
s1=[]
if(m<n) or (m-n)<3 or m<0 or n<0 or n>8:
    print("illegal input")
else:
    for x in range(n,m):
        s.append(x)
    for x in range(len(s)):
        for y in range(len(s)):
            for z in range(len(s)):
                if x!=y and y!=z and x!=z and s[x]!=0:                   
                    s1=str(s[x])+str(s[y])+str(s[z])
                    if s1 not in s1:
                        s1.append(s1)
                    else:
                        pass
                else:
                    pass
                   
    for y in s1:
        y=int(y)
        print("%d "%y,end="")

