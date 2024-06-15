lst=eval(input())
lst2=[]
for x in lst:
    k=0
    for y in range(1,x+1):
        if x%y==0:
            k+=1
    if k == 2:
        lst2.append(x)
print(lst2)
    
            
