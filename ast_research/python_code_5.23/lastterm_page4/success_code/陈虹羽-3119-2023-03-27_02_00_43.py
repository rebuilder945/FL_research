a=eval(input())
b=a.copy()
for i in a:
   if b.count(i)!=1:
       b.remove(i)
print(b)
        
