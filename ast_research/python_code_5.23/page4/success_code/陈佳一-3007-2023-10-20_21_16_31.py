lst=eval(input())
n,m=eval(input())
if m in lst and n in lst:
   del lst[n:m]
   print(lst)
else :
    print("error")
