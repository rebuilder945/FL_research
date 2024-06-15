n=eval(input())
c=[]
while 100<n<1000:
 for i in range(len(n)):
   for x in range(100,n):
    b=x%10
    h=b**3
    c.append(h)
    if sum(c)==n:
     print(h)
else:
    print("none")
  



