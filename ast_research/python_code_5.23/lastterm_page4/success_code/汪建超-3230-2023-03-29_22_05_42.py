list1=eval(input())
list1.sort(reverse=True)
list2=list(range(len(list1)))
list3=[]
i=-1
for x in list1:
    list3.append(x*10**list2[i])
    i-=1
print(sum(list3))  


