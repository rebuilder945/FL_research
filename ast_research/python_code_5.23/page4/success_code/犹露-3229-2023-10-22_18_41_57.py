a = eval(input())
b =[]

for i in a:
    if a.count(i)==1:
        b.append(i)
        b.sort()
 

list1  = ','.join (str(i) for i in b)
if b==[]:
   list1 = "False"
print(list1) 





    
        




