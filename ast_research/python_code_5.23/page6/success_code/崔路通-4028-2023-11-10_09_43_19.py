n=eval(input())
if not (type(n)==int and n>1):
    print("illegal input")
else:
   a=[]
   b=[c for c in range(2,n+1)]
   for i in range(2,n+1):
       for x in range(2,i):
           if i%x==0:
               a.append(i)
   for d in b:
       if d not in a:
           print(d,end=" ")
   
           
    
