lit=list(map(eval,input().split(',')))
n,m=eval(input())
if abs(n)>len(lit):
    print('error')
else:
    lit.extend([lit[n]]*m)
    print(lit)
