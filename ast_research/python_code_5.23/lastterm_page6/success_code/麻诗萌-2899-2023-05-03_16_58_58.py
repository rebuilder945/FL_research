def stu(x,y):
    if x>=y:
        print("illegal input")
    else:
        lst0=[]
        lst3=[]
        for i in range(x,y):
            lst0.append(str(i))
            if len(lst0)<3:
                print("illegal input")
            else:
                for i in lst0:
                    s=i
                    lst1=lst0.copy()
                    lst1.remove(i)
                    for i in lst1:
                        s=s+i
                        lst2=lst1.copy()
                        lst2.remove(i)
                        for i in lst2:
                            s=s+i
                            lst3.append(s)
        print(lst3)
n,m=map(int,input().split(" "))
stu(n,m)


