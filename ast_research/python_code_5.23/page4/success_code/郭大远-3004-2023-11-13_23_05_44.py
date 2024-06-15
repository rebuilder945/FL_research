a=eval(input())
c=0
h=[]
for b in a:
    for i in range(1,b+1):
        if b%i==0:
           c+=1
        if c==2:
         h.append(b)
print(h)


         
          

