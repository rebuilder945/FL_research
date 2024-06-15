list_1 =input().split(" ")
list_2 =input().split(" ")
n=int(list_2[0])
m=int(list_2[1])
# list_2= list_1.copy()
a=list_1[n]
b=list_1[m]
list_1[n]=b
list_1[m]=a
print(list_1)
