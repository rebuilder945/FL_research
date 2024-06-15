list1=input()
list2=eval(input())
list3=list(list1)
new=[]
for i in range(len(list2)):
    list3="'"+str(list3[i:i+1])+"'"+","+str(list2[i])
    list4=eval(list3)
    list5=[list4]
    new.append(list5)
print(new)

    




