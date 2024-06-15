list1=input()
list2=eval(input())
list3=list1.split(",")
list4=str(list3).strip('[]')
new=[]
for i in range(len(list2)):
    list5=list4[i:i+1]+","+str(list2[i])
print(list5)

    




