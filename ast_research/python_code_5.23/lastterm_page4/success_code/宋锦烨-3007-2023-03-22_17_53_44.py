liebiao=eval(input())
n,m=eval(input())
n=int(n)
m=int(m)
if n>len(liebiao) or m>len(liebiao):
    del liebiao[n:m]
    print(liebiao)
else:
    print(error)

