def left(ls,k):
    tem=ls
    for i in range(0,k):
        tem.append(tem.pop(0))
    return tem
import left
n=eval(input())
num=range(1,n+1)
ls=list(num)
k=1
print(left.left(ls,k))
