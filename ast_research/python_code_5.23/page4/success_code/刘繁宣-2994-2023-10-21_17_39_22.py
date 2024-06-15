ls=list(map(int,input().split(",")))
n,m=eval(input())
if n>=0 and n+1<=len(ls):
    ls2=[ls[n] for i in range(m)]
    print(ls+ls2)
elif n<0 and -n<=len(ls):
    ls3=[ls[n] for i in range(m)]
    print(ls+ls3)
else:
    print("error")
