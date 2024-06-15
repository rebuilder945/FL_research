n=eval(input())
f=True
if n<0 or int(n)!=n:
    print("illegal input")
else:
    if n>=2:
        print("2",end=" ")
        for i in range(2,n):
            for j in range(2,i):#验证素数
                if i%j==0:
                    f=True
            if not f:
                for k in range(len(str(i))//2):#验证回文数
                    if str(i)[k]!=str(i)[-k-1]:
                        f=True
                if not f:
                    print(i,end=" ")
            f=False
