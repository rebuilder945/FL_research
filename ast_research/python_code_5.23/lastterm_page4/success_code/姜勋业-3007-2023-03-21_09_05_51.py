lst=eval(input())
n,m=eval(input().split(","))
if m<=len(lst):
   del lst[n,m]
   print(lst)
else:
   print("error")
   
