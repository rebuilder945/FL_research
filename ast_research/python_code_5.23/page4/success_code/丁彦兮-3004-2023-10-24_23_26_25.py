a= eval(input())
# c=[]
for i in a:
    if i==2 :
       pass
    if i==0 :
      a.remove(i)
    if i==1 :
      a.remove(i)
    else:
       for x in range(2,i):
        if i%x==0 :
         a.remove(i)  
         break
        else:
         pass
print(a)
    





