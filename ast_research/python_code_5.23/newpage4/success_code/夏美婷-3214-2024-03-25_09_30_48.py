# list1=eval(input())
# list2=[]
# for i in list1:
#     if i==0:
#         list2.append(i)
#         list1.remove(i)
# for i in list1:
#     if i==0:
#         list2.append(i)
#         list1.remove(i)
# list3=list1+list2
# print(list3)        
list1=eval(input())
list2=[]
for i in list1:
    if i==0:
        list2.append(i)
while 0 in list1:
    list1.remove(0)
list3=list1+list2
print(list3)
