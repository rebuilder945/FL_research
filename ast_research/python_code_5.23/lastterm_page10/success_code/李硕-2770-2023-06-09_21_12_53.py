list1="abcdefghijklmnopqrstuvwxyz"
list2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x=str(input())
new=[]
for i in range(27):
    for j in range(27):  
         if x[i]==list1[j]:
              new.append(list2[26-j])  
         elif x[i]==list2[j]:
              new.append(list1[26-i])
         else:
              new.append(x[i])
t=''.join(new)   
print(t)       

