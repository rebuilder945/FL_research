ls1=input().split(',')
(n,m)=eval(input())
ls2=[]
for i in range(len(ls1)):
    ls2.append(ls1[i])
if n>=len(ls1) or -n>=len(ls1):
    print('error')
else:
    for i in range(m):
        ls2.append(int(ls1[n]))
    print(ls2)
