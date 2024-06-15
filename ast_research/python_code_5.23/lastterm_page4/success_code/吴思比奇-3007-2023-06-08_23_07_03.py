list=eval(input())
n,m=eval(input())
l=len(list)
if m>n :
    del list[n:m]
    print(list)
elif n==m:
    x=n
    del list[n]
    print(list)
if m<n:
    print('error')

    



