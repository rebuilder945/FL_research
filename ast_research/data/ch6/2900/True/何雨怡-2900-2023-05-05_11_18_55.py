n=eval(input())
sushu=[]
if n<=0 or type(n)!=int:
    print("illegal input")
else:
    for i in range(1,n+1):
        if i==2:
            sushu.append(2)
        elif i==1:
            pass
        else:
            for x in range(2,i):
                if i%x==0:
                    break
            else:
                sushu.append(i)
    huiwensushu=[]
    for i in sushu:
        string=str(i)
        if string==string[::-1]:
            huiwensushu.append(i)
            print(i,end=" ")
        else:
            pass
