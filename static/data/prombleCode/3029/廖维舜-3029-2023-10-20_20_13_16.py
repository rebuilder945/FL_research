list1=input().split(',')
list2=eval(input())
new=[]
for i in range(len(list2)):
    list3="'"+list1[i:i+1]+"'"+","+str(list2[i])
    list4=eval(list3)
    list5=[list4]
    new.append(list5)
print(new)

    




