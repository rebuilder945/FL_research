from re import A


a=input()
b=eval(input())
a=a.split(",")
list=[]
c=len(a)
for i in range(c):
    list1=[]
    list1.append(a[i])
    list1.append(b[i])
    list.append(list1)
print(list)
