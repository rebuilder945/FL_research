l=list(eval(input()))
n,m=eval(input())
if -len(l)<=n<=len(l):
    l=l+[l[n]]*int(m)
    print(l)
else:
    print(error)
