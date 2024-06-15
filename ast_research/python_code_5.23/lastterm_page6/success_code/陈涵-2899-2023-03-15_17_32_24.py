n,m=map(int,input().split(" "))
if n>=m:
    print("illegal input")
else:
    num=[]
    s=[str(i) for i in range(n,m)]
    for i in range(len(s)):
        for x in range(len(s)):
            for y in range(len(s)):
                a=[s[i],s[x],s[y]]
                num.append("".join(a))
    for i in range (len(num)-1):
        if len(num[i])>3:
            del num[i]
        elif num[i][0]==0:
            del num[i]
        else:
            if num[i][1]==num[i][2] or num[i][0]==num[i][1] or num[i][0]==num[i][2]:
                del num[i]
    if num==[]:
        print("illegal input")
    else:
        print(" ".join(num))                







