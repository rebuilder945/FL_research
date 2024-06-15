l=list(eval(input()))
n,m=eval(input())
if n>0 and n>len(l):
    print("error")
elif n<0 and abs(n)>len(l):
    print("error")
else:
    a=l[n]*m
    l=l+a
    print(l)
