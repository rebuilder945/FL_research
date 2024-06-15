lit=eval(input())
n,m=eval(input())
if n>len(lit) or n>m:
    print('error')
else:
    for i in range(n,m):
        lit.pop(i)
    print(lit)
