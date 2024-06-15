n=eval(input())
if n<=0 or type(n)==float:
    print("illegal input")
else:
    def sushu(a):
        if a==2:
            return True
        if a>2:
            for i in range(2,a):
                if a%i==0:
                    return False
            return True
    def huiwenshu(a):
        a1=str(a)
        a2=a1[::-1]
        if a1==a2:
            return True
    for i in range(2,n+1):
        if sushu(i) and huiwenshu(i):
            print(i,end=' ')
