ll=list(input().split(','))
n,m=eval(input())
if n>=len(ll) or n<-len(ll):
    print('error')
else:
    for i in range(m):
        ll.append(ll[n])
    print(str(ll).replace("'",""))

