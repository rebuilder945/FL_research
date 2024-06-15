lst=eval(input())
lst2=[]
for i in lst:
    for x in range(2,i):
        if not i%x==0:
          lst2.append(i)  
print(lst2)

    
