lst1 = eval(input())
n,m = eval(input())
if n < len(lst1) and m < len(lst1):
    if n<m:
        del lst1[n:m]
        print(lst1) 
    elif n==m:
        print(lst1)
    else:
        print('error')
else:
    print('error')
