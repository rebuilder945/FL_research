num=eval(input())
shuixianhua=[]
if 100<num<1000:
    for i in range(100,num+1):
        a=int(str(i)[0])
        b=int(str(i)[1])
        c=int(str(i)[2])
        if a**3+b**3+c**3==i:
            shuixianhua.append(i)
        else:
            continue
    if shuixianhua==[]:
        print("none")
    else:
        for i in shuixianhua:
            print(i)
elif num>=1000:
    for i in range(100,1000):
            a=int(str(i)[0])
            b=int(str(i)[1])
            c=int(str(i)[2])
            if a**3+b**3+c**3==i:
                shuixianhua.append(i)
            else:
                continue
    if shuixianhua==[]:
        print("none")
    else:
        for i in shuixianhua:
            print(i)
else:
    print("none")
