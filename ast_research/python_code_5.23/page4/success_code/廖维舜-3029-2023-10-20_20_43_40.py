list1=input()
list2=eval(input())
list1.split("")
new=[]
for i in range(len(list2)):
    list3="'"+str(list1[i:i+1])+"'"+","+str(list2[i])
    list4=[list3]
    new.append(list4)
print(new)

    




