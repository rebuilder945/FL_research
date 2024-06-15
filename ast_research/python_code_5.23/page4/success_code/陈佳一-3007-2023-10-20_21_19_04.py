lst=eval(input())
n,m=eval(input())
if m-1 in lst and n-1 in lst:
   del lst[n:m]
   print(lst)
else :
    print("error")
