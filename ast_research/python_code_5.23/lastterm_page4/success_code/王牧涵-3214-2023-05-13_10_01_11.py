list1=eval(input())
list3=list1.copy()
list2=[]
w=0
for x in list1:
    if x==0:
        list3.remove(0)
        w+=1

while w>0:
    list3.append(0)
    w-=1
print(list3)


