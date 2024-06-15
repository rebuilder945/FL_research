ss=input().split(" ")
a,b=input().split(" ")
a=int(a)
b=int(b)
ss=list(ss)
ss[a],ss[b]=ss[b],ss[a]
print(ss)
