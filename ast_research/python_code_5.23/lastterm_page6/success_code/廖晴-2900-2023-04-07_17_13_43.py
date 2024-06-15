n=int(input())

if n<=0 or type(n)==float:
    print("illegal input")
else:
    def sushu(i):
        if i>1:
            if i==2:
                return 2
            for x in range(2,i):
                if i%x==0:
                    break
                else:
                    return i
    def huiwen(i):
        i1=str(i)
        i2=i1[::-1]
        if i1==i2:
            return i
    for i in range(2,n+1):
        if sushu(i) and huiwen(i)==i:
            print(i,end=" ")     







    #        s=[]
    # for i in range(1,n+1):
    #     s.append(i)
    #     for x in range(2,i):
    #         if i%x==0:
    #             s.remove(i)
    #             break
    # for y in s:
    #     y1=str(y)
    #     if y==y1[::-1]: 
