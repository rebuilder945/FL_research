lst = eval(input())
n,m =eval(input())
a = len(lst)
if n>m or n+1 > a or m +1> a:
   print ("error")
else :
   del lst[n:m]
   print(lst)
