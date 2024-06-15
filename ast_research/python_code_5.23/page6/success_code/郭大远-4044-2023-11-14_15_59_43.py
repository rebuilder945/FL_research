n=eval(input())
c=[]
while 100<n<1000:
    for x in range (100,n):
       for i in range(3):
         b=x%10
         h=b**3
         x=x//10
         c.append(h)
         if sum(c)==n:
            print(h)
else:
    print("none")
  



