cao=eval(input())
n,m=eval(input())
if n<0 or m>len(cao)-1:
    print('error')
elif n==m-1:
    del cao[n]
else:
    for i in range(n,m):
        del cao[n]
    print(cao)
