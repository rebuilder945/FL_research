a=eval(input())
c=[]
d=[]
for i in a:
    b=a.count(i)
    if b==1:
        c.append(i)
    if b!=1:
        d.append(i)
        if a==d:
            print('False')
print(c)


        
         
