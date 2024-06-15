num=eval(input())
lis=[]
if type(num)==int and num>0:
    for x in range(2,num):
        a=str(x)
        b=a[::-1]
        if a==b:
            for y in range(2,x):
                if x%y==0:
                    break
            else:
                lis.append(x)
    for q in lis:
        print(q,end=" ")
else:
    print("illegal input")
