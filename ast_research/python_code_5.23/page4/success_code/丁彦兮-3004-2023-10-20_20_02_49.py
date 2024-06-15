a= eval(input())
c=[]
for i in range(len(a)):
    b=a[i]
    for x in range(2,b):
        if b%x!=0 :
         c.append(b)  
         break
        else:
         pass
print(c)
    



