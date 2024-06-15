lit=eval(input())
n,m=eval(input())
if max(n,m)>=len(lit) :
    print('error')
else:
    for i in range(n,m):
        lit.pop(i)
    print(lit)


