n=eval(input())
if str(n).find(".")!=-1 and n<=1:
    print("illegal input")
else:
    ls1=[]
    for i in range(2,n):  
        for j in range(2,i):
            if i%j==0:
               break
        else:
            ls1.append(i)  
    ls2=[]
    for x in ls1:
        if str(x)==str(x)[::-1]:
           ls2.append(x)
    for e in ls2:
        print(e,end=' ')


