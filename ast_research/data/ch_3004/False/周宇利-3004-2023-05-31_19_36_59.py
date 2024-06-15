a=eval(input())
b=[]
for i in a:
    num=0
    for x in range(1,i+1):
        t=i/x
        if t%1==0:
            num+=1
            if num==2:
                b.append(i)
    print(b)
