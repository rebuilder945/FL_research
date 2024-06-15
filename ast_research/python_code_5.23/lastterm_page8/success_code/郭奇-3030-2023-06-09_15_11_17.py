lst1=input().split(',')
lst2=input().split(',')
lst3=[]
dit={}
for i in range(len(lst1)):
    lst4=[]
    lst4.append(lst1[i])    
    lst4.append(int(lst2[i]))
    lst3.append(lst4)
print(lst3.sort(key=lambda x: x[1]))
