n=eval(input())
if type(n)==int and n>0:
    x=[] 
    for i in range(2,n):
        for j in range(2,i,1):
            if i%j==0:
                break
        else:
            x.append(i)
    for i in x:
        m=str(i)[-1::-1]
        if str(i)==m:
            print(i,end=" ")
else:
    print("illegal input")
