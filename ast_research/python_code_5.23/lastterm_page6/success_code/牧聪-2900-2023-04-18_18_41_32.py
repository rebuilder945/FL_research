def found(n):    
    list=[]
    for x in range(2,n):
        t=str(x)
        tt=t[::-1]
        if t==tt:
            num=[]
            for i in range(2,x-1):
                if x%i!=0:
                    num.append(0)
                else:
                    num.append(1)
            if sum(num)==0:
                list.append(x)
    print(" ".join(str(q) for q in list))
n=input()
for o in n:
    if o=="-":
        print("illegal input")
        break
    elif o==".":
        print("illegal input")
        break
    elif o==0:
        print("illegal input")
        break
    elif o==n[-1]:
        n=int(n)
        found(n)


    



                

