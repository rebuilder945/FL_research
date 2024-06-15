list=eval(input())
n,m=eval(input())
l=len(list)
if m>n :
    for x in range(n,m):
        list.pop(x)
        print(list)
if n==m:
    x=n
    del list[n]
    print(list)
if m<n:
    print('error')

    

