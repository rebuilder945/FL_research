n1=eval(input())
n2=[]
for x in n1:
    if x!=0:
        n2.append(x)
for i in range(len(n1)-len(n2)):
    n2.append(0)
print(n2)
    
        

