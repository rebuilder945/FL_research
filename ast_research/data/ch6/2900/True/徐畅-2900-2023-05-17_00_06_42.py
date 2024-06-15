def sushu(i):
    a=0
    for y in range(2,i//2+2):
        
        if i%y==0:
            a=a+1
    return a

        

def huiwen(i):
    lst1=list(str(i))
    lst2=lst1.copy()
    lst1.reverse()
    if lst1==lst2:
        return 1
    else :
        return 0
n=eval(input())
if n<=1 or type(n)!=int:
    print("illegal input")
else:
    lst=[2]
    for x in range(2,n+1):
        if sushu(x)==0 and huiwen(x)==1:
            lst.append(x)
    print(*lst,sep=' ')



    




