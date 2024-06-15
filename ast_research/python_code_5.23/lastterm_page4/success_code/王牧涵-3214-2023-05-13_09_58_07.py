list1=eval(input())
list2=[]
w=0
for x in list1:
    while x==0:
        list1.remove(0)
        w+=1
list3=list1.copy()
while w>0:
    list3.append(0)
    w-=1
print(list3)


