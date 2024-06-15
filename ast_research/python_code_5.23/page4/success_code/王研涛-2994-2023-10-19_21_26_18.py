a=eval(input())
b=list(a)
n,m=eval(input())
c=b.copy()
for i in range(m):
   b.append(a[n])
if n>len(a)-1:
   print("error")
else:
    print(b)
