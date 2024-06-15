a=eval(input())
n,m=eval(input())
if n>len(a) or m>len(a) or n>m:
    print('error')
else:
    del a[n:m]
    print(a)
            



    
