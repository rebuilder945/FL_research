a=eval(input())
b=[]
for i in a:
    if i>=10:
          if i%3!=0 or i%2!=0 or i%5!=0 or i%7!=0:
               b.append(i)
    else: 
         if i==2 or i==3 or i==5 or i==7:
              b.append(i)
print(b)
