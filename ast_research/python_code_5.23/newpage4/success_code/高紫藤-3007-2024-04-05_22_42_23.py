a = eval(input())
n,m = eval(input())
if m <= len(a):
   del a[n:m]
elif m > len(a):
   print("error")
print(a)





