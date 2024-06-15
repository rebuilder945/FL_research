def permutation(s,level):
    if level==len(s):
        a=''.join(str(i) for i in s)
        if int(a) >=100:   
            print(a)
        else:
            pass
    for i in range(level,len(s)):
        s[level],s[i]=s[i],s[level]
        permutation(s,level+1)
        s[level],s[i]=s[i],s[level]
n,m=map(int,input().split())
jack=[]
for i in range(n,m):
    jack.append(i)
l=''.join(str(i) for i in jack)
if len(l) !=3:
    print("illegal input")
else:
    s=list(l)
    permutation(s,0)
