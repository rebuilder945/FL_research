list=eval(input())
n,m=eval(input())
if m>n :
    for x in range(n,m):
        list.pop(x)
        print(list)
if n==m:
    list.pop(n)
if m<n:
    print('error')
        
    

