lst = eval(input())
n,m = eval(input())
if n<len(lst) and m<len(lst):
  for i in range(n,m):
    lst.remove(lst[i])
    print(lst)
elif n>len(lst) or m>len(lst):
  print("error")
 
  
    


