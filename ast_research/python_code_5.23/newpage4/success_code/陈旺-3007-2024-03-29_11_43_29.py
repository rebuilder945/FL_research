a=input()
a=a.strip("[")
a=a.rstrip("]")
b=[int(i) for i in a.split(",")]
m,n=eval(input())
if m<=len(b) and n<=len(b):
   if m>n:
      del b[n:m]
   if m<n:
      del b[m:n]
   print(b)
else:
    print("error")
