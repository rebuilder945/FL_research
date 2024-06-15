lst=eval(input())
n,m=input().split(",")
n=int(n)
m=int(m)
k=len(lst)
if m<k-1:
   for i in range(n,m):
       del lst[i]
   print(lst)
else:
   print("error")
   
