liebiao=eval(input())
n,m=eval(input())
n=int(n)
m=int(m)
if n<len(liebiao) and m<len(liebiao):
    del liebiao[n:m]
    print(liebiao)
else:
    print('error')

