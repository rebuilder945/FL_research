a=eval(input())
b=[]
for i in a:
        c=2
        if i>c and i%c==0:
            a.remove(i)
        elif i>c and i%c!=0:
              c+=1
        elif c>=i:
              break       
print(a)

