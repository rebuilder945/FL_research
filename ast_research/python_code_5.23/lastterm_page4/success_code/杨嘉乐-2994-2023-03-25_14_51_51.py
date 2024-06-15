ll=list(input().split(','))
lll=ll
n,m=eval(input())
if n>=len(ll) or n<-len(ll):
    print('error')
else:
    for i in range(m):
        ll.append(lll[n])
    print(str(ll).replace("'",""))

