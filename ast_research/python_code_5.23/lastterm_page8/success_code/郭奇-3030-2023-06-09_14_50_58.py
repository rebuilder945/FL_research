lst1=input().split(',')
lst2=input().split(',')
lst3=[]
for i in range(len(lst1)):
    lst4=lst1[i]+lst2[i]
    lst3.append(lst4)
    lst3.sort(key=int(lst4[1]))
print(lst3)
