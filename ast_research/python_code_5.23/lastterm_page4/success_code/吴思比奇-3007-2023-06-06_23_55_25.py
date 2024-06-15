list=eval(input())
n,m=eval(input())
if m>n :
    for x in range(n,m):
        list.pop(x)
        print(list)
if m<n:
    print('error')
else:
    list.pop(n)
    print(list)
        
    

