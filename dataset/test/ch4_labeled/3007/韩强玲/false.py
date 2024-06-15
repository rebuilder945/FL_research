lst = eval(input())
n,m =eval(input())
a = len(lst)
if n>m and n+1 > a and m +1> a:
   print ("error")
else :
   del lst[n:m]
   print(lst)
