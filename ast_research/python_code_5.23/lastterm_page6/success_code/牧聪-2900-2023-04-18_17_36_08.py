n=int(input())
list=[]
if n<=0:
    print("illegal input")
else:
    for x in range(n):
        t=str(x)
        tt=t[::-1]
        if t==tt:
            num=[]
            for i in range(2,x-1):
                if x%i!=0:
                    num.append(0)
        if sum(num)==0:
            list.append(x)
print("".join(str(q) for q in list))


                

