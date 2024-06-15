a=list(map(int,input().split(',')))
n,m=eval(input())
b=[]
if n<=len(a):
   c=a[n]
   b.append(c)
   print(a+m*b)
else:
   print("error")
