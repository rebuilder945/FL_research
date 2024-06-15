list1=input()
list2=eval(input())
list3=list(list1)
new=[]
for i in range(len(list2)):
    list4="'"+list3[i:i+1]+"'"+","+list2[i]
    list5=[list4]
    new.append(list5)
print(new)

    




