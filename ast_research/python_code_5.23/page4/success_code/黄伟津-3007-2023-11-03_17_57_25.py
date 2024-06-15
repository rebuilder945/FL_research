l = eval(input())
n,m = eval(input())
if n>len(l)-1 or m>len(l)-1:
     print("error")
else:
     if n>m:
         del l[m+1:n+1]
         print(l)
     else:
          del l[n:m]
          print(l)
