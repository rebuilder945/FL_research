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
    num2=[]
    num3=[]            
    if num==[]:
        print("illegal input")            
    else:
        for i in range(len(num)):
            if int(num[i][0])!=0:
                num2.append(num[i])
        for i in range(len(num2)):
            if num2[i][0]!=num2[i][1] and num2[i][0]!=num2[i][2] and num2[i][1]!=num2[i][2]:
                num3.append(num2[i])
        if num3==[]:
            print("illegal input")
        else:
            print(" ".join(num3))                  







