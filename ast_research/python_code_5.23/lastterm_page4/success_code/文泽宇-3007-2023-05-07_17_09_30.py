cao=eval(input())
n,m=eval(input())
if n<0 or m>len(cao)-1 or n>m:
    print('error')
else:
    for i in range(n,m):
        del cao[n]
    print(cao)
