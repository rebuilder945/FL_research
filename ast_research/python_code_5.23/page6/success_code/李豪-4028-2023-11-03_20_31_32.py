n=eval(input())
b=[]
if n<0 and n%1!=0 :
    print("illegal input")
for i in range(1,n+1):
    for m in range(2,n+1):
        if m!=i and m!=1:
            i%m!=0
            num=str(i)
            x=num[::-1]
            if x==num:
                j=int(x)
                b.append(j)
for k in range(len(b)):
    print("%d"%b[k],end='')

                  
    

