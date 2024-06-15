lst1=input().split(',')
lst2=eval(input())
lst3=list(lst1)
lst4=()
lst5=[]
for i in range(len(lst3)):
    lst4=(lst3[i],lst2[i])
    lst5.append(list(lst4))
print(lst5)    
