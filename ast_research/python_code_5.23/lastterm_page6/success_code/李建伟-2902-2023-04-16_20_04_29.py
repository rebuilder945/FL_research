n = eval(input())
lst = [1,1]
for x in range(n):
    a = lst[-1]+lst[-2]
    lst.append(a)
lst1 = lst[1::]
lst2 = lst[2::]
sum = 0
for i in range(n):
    sum = sum+lst2[i]/lst1[i]
print("%.4f"%(sum))
