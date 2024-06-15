list1=input()
list2=eval(input())
new=[]
for i in range(len(list2)):
    list3="'"+list1[i:i+1]+"'"+","+str(list2[i])
    list5=[list3]
    new.append(list5)
print(new)

    




