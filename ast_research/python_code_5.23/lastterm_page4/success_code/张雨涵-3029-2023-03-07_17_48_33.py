list1=input()
list2=eval(input())
list3=[]
for i in range (len(list2)):
    m=[list1[2*i],list2[i]]
    list3.append(m)
print(list3)
