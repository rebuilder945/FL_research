a=eval(input())
ls1=[]
for i in a:
    for j in range(1,i):
        if i%j!=0:
           ls1.append(i)
           break
print(ls1)
            
