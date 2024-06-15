n=eval(input())
if not (type(n)==int and n>1):
    print("illegal input")
else:
   a=[]
   b=[c for c in range(2,n+1)]#b是所有数
   for i in range(2,n+1):
       for x in range(2,i):
           if i%x==0:
               a.append(i)#a是不是素数的数
   e=b.copy()
   f=[]
   for d in e:
       if d>9:
           for i in range(len(str(d))):
               if str(d)[i]==str(d)[len(str(d))-i]:
                   f.append(d)
       if d<=9:
           f.append(d)
   for x in f:
       if x not in a:
           print(x,end=" ")
           
        
                   
           
   
   
           
    
