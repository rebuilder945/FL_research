def sushu(x):
    lst1=list(range(2,x))
    a=0
    for x1 in lst1:
        if x%x1==0:
            a=a+1
    if a==0:
        return 1
    else:
        return 0
def huiwen(x):
    lst2=list(str(x))
    lst3=lst2.copy()
    lst2.reverse()
    if lst3==lst2:
        return 1
    else:
        return 0
n=eval(input())
if type(n)!=int or n<=0:
    print("illegal input")
else:
    lst4=[]
    for i in range(2,n+1):
        if (sushu(i))+(huiwen(i))==2:
            lst4.append(i)
    lst4.sort() 
    print(*lst4,sep=" ")
    
