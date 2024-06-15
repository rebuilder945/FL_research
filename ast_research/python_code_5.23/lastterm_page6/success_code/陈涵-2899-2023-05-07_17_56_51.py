n,m=map(int,input().split(" "))
if n>=m:
    print("illegal input")
else:
    num=[]
    s=[str(i) for i in range(n,m)]
    for i in range(len(s)):
        if s[i]!="0":
            for x in range(len(s)):
                if s[x]!=s[i]:
                    for y in range(len(s)):
                        if s[y]!=s[x] and s[y]!=s[i] and len(s[i]+s[x]+s[y])==3:
                            num.append(s[i]+s[x]+s[y])
if num==[]:
    print("illegal input")
else:
    for x in num:
        print(int(x),end=' ')                                                 
                



