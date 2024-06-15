lst = eval(input())
n,m = eval(input())
if n<=len(lst) and m<=len(lst) and n<=m:
  del lst[n:m]
  print(lst)
elif n<=len(lst) and m<=len(lst) and n>m:
  del lst[m,n]
  print(lst)
elif n>len(lst) or m>len(lst):
  print("error")
 
  
    


