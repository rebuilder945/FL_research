a = eval(input())
n,m = eval(input())
if m <= len(a) and n <=len(a) and n <= m:
   del a[n:m]
   print(a)
elif m > len(a) or n <= len(a) or n > m:
   print("error")






