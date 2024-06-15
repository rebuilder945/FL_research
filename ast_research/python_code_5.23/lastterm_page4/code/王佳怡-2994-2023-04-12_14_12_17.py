l=list(eval(input()))
n,m=eval(input())
if -len(l)<=n<=len(l):
    l1=[l[n for i in range(m)]]
    print(l+l1)
else:
    print("error")
    
