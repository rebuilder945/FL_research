a=eval(input())
a.sort()
b=[]
for i in a:
    if a.count(i)==1:
       b.append(i) 
print(b)
   

