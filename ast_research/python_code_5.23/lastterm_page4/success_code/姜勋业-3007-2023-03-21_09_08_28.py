lst=eval(input())
n,m=input().split(",")
n=int(n)
m=int(m)
k=len(lst)
if m<=k:
   del lst[n,m]
   print(lst)
else:
   print("error")
   
