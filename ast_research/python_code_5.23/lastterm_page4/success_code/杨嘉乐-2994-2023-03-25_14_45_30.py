ll=list(input().split(','))
m,n=eval(input())
if n>len(ll):
    print('error')
else:
    for i in range(n):
        ll.append(ll[m])
    print(str(ll).replace("'",""))

