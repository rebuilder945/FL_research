lst=eval(input())
n,m=input().split(",")
k=len(lst)
if m<=k:
   del lst[n,m]
   print(lst)
else:
   print("error")
   
