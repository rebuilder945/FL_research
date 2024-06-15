n=eval(input())
lst1=[2,3]
for i in range(n):
    lst1.append(lst1[i]+lst1[i+1])
lst2=[1,2]
for i in range(n-len(lst2)):
    lst2.append(lst2[i]+lst2[i+1])
lst3=[]
for i in range(n):
    lst3.append(lst1[i]/lst2[i]) 
print("%.4f"%sum(lst3))

