num=int(input())
ls=[]
if num>=100:
    for i in range(100,num+1):
        s=str(i)
        a=int(s[0])
        b=int(s[1])
        c=int(s[2])
        if a**3+b**3+c**3==i:
            print(i)
            ls.append(i)
            if len(ls)==0:
                print("none")
else:
    print("none")
