lst1=map(list,input().split(','))
lst2=eval(input())
lst3=[]
for i in range(len(lst1)):
    lst0=[]
    lst0=[lst1[i],lst2[i]]
    lst3.append(lst0)
print(lst3)
