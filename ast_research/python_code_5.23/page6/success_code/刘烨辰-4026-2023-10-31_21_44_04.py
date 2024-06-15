n = eval(input())
list1 = [2,3]
for i in range(0,n-2):
    a = list1[i] + list1[i+1]
    list1.append(a)
list2 = [1,2]
for i in range(0,n-2):
    b = list2[i] + list2[i+1]
    list2.append(b)
sum = 0
for i in range(0,n):
    sum = int(list1[i])/int(list2[i]) + sum
print("%.4f"%sum)
print(list1,list2)
