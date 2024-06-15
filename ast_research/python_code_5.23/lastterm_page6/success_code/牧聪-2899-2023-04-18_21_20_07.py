a=input()
lst=a.split(" ")
n,m=int(lst[0]),int(lst[1])
if "-"in a:
    print("illegal input")
elif "."in a:
    print("illegal input")
elif m-n<=2:
    print("illegal input")
elif m>=12:
    print("illegal input")
else:
    lst1=[x for x in range(n,m)]
    if m-1!=10:
        nums=[]
        for i in lst1:
            lst2=[t for t in lst1 if t!=i]
            for t in lst2:
                lst3=[s for s in lst2 if s!=t]
                for s in lst3:
                    num=str(i)+str(t)+str(s)
                    nums.append(num)
        print(nums)
