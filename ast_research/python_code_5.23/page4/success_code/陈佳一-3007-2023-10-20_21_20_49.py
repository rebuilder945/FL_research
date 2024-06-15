lst=eval(input())
n,m=eval(input())
a=len(lst)
if m<=a and n<=a:
   del lst[n:m]
   print(lst)
else :
    print("error")
