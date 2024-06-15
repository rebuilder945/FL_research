def shift(lst):
list2=list(list1)
list3=[]
for i in list2[:len(list2)-1]:
    list3.append(i)
    list3[0]=list2[-1]
return(list3)

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

