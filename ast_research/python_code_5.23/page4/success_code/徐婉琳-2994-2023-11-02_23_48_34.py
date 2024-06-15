c=eval(input())
f=list(c)
n,m=eval(input())
if 0<=n<=len(f)-1 or -len(f)<=n<=-1:
   h=[]
   h.append(f[n])
   l=h*m
   print(f+l)
else:
   print('error')

