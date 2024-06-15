list1=input()
list2=eval(input())
list3=list(list1)
new=[]
for i in range(len(list2)):
    list4="'"+str(list3[i:i+1])+"'"+","+str(list2[i])
    list5=eval(list4)
    list6=[list5]
    new.append(list6)
print(new)

    




