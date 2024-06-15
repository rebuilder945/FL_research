a  = eval(input())
a = list(a)
n,m=eval(input())
if n>=len(a) or a<-len(a):
    print('error')
else:
    for i in range(m):
        a.append(a[n])
    print(a)
