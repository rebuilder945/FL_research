a= eval(input())
n,m= eval(input())
b= len(a)
if m and n>b-1:
   print("error")
else:
    del a[n:m]
    print(a)

