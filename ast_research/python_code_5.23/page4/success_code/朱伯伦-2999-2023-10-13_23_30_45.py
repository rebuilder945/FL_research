list=input().split(" ")
list3=input().split(" ")
n=int(list3[0])
m=int(list3[1])
list2=[list[n],list[m]]
list[n]=list2[1]
list[m]=list2[0]
print(list)
