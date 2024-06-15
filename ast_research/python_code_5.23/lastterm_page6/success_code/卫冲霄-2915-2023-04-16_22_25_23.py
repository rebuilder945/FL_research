num=int(input())
if num>=100:
    for i in range(100,num+1):
        s=str(i)
        a=int(s[0])
        b=int(s[1])
        c=int(s[2])
        if a**3+b**3+c**3==i:
            print(i)
else:
    print("none")
