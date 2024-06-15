n=eval(input())
list=[]
m=str(n)
for o in m:
    if o=="-" or o==".":
        print("illegal input")
    elif o==m[-1]:
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


                

