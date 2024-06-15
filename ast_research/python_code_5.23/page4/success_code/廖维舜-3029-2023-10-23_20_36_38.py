list1=input()
list2=eval(input())
list3=list1.split(",")
new=[]
for i in range(len(list2)):
    list5=list3[i:i+1]
    list6="'"+str(','.join(list5[0:1]))+"'"+","+str(list2[i])
    list7=eval(list6)
    list8=[list7]
    new.append(list8)
print(new)

    








