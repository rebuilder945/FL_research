a=eval(input())
c=0
h=[]
for x in a:
    for i in range(1,x+1):
        if x%i==0:
            c+=1
    while c==2:
        h.append(x)
print(h)


         
          

