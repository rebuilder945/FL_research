lst=[1,2]
lst2=[]
n=eval(input())
for i in range(n-1):
    lst.append(lst[-1]+lst[-2])
for i in range(n):
    lst2.append(lst[i+1]/lst[i])
print(f'{sum(lst2):.4f}')

