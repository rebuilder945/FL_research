list1=list(input())
while "," in list1:
    list1.remove(",")
list2=eval(input())
list3=[]
for i in range(0,len(list1)):
    list3.append([list1[i],list2[i]])
print(list3)   

