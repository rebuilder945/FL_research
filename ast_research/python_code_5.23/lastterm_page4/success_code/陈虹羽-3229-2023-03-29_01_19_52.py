a=eval(input())
a.sort()
b=[]
for i in a:
   c=a.count(i)
   if c==1:
      b.append(i)
if b==[]:
   print("False")
else:
   print(b)
      
