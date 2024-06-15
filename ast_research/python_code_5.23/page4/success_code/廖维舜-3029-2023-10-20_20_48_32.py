list1=input()
list2=eval(input())
list3=list1.split(",")
new=[]
for i in range(len(list2)):
    list4="'"+str(list3[i:i+1])+"'"+","+str(list2[i])
    list5=[list4]
    new.append(list5)
print(new)

    




