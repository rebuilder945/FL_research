import copy
ll=list(input().split(','))
lll=copy.deepcopy(ll)
n,m=eval(input())
if n>=len(ll) or n<-len(ll):
    print('error')
else:
    for i in range(m):
        ll.append(lll[n])
    print(str(ll).replace("'",""))

