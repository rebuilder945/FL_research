#判断素数
def sushu(n):
    a=0
    if n<=1:
        return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                a=1
                break
        if a==0:
            return 1
        if a==1:
            return 0
#判断回文数
def huiwen(n):
    import copy
    m=str(n)
    l=copy.deepcopy(m)
    l=reversed(l)
    if l==m:
        return 1
    else:
        return 0
#挨个筛选
n=eval(input())
if n<0 or isinstance(n,int)==False:
    print('illegal input')
else:
    for x in range(2,n+1):
        if sushu(x)==1 and huiwen(x)==1:
            print(x,end=" ")
