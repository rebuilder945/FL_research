m=input()
for x in m:
    if "a"<=x<="z" or "A"<=x<="Z":
        m1=x.count(m)
        print(m1)
    elif x==(" "):
        m2=x.count(m)
        print(m2)
    elif 0<=x<=9:
        m3=x.count(m)
        print(m3)
    else:
        m4=x.count(m)
        print(m4)

