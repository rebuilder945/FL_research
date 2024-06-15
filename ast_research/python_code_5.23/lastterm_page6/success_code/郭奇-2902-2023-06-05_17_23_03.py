n=eval(input())
lst1=[2,3]
for i in range(n):
    lst1.append(lst1[i]+lst1[i+1])
lst2=[]
for i in range(n):
    lst2.append(lst1[i]/(i+1))
print("%.4f"%sum(lst2))

