stu=input().split()
a=eval(stu[1])
b=eval(stu[2])
c=eval(stu[3])
avg=(a+b+c)/3
list1=[]
list2=[]
list2.append(a)
list2.append(b)
list2.append(c)
list2.sort(reverse=True)
for i in range(3):
    list1.append(list2[i])
list1.append(avg)
print(stu[0],end=" ")
for i in list1:
    print("%.2f"%i,end=" ")
