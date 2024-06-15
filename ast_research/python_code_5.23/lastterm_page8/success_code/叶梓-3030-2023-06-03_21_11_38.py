list1=input().split(',')
list2=input().split(',')
list3=[]
i=0
for x in list1:
    list3.append(x,eval(list2[i]))
    i+=1
print(sorted(list3,key=lambda x:(x[1],x[0]))) #

