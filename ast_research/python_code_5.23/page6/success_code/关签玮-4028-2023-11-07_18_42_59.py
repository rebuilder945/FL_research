def sushu(a):
    ls=[]
    for i in range(2,a//2+2):
        if a%i==0:
            ls.append(a)
    return(ls)

n=eval(input())
for i in range(3,n+1):#取数
    if sushu(i).count(i)==0 and str(i)==str(i)[::-1]:
        print(i,end=" ")

