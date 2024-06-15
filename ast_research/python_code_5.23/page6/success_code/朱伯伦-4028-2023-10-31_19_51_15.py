n=eval(input())
s=''
ls1=[] 
ls2=[]
if n<=1:
    print('illegal input')
else:
    while(n>1):
        for i in range(n):
            if str(i)[::-1]==str(i):
                ls1.append(i)

    for i in range(n):
        for x in range(2,i):
            if i%x==0:
                ls2.append(x)
    for i in range(n):
        if (i in ls1 and i in ls2):
            s+='%s '%(str(i))
    print(s)



