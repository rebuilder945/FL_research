list1=eval(input())
list2=[]
for x in list1:
    if list1.count(x)==0:
        print("False")
    if list1.count(x)==1:
        list2.append(x)
list2.sort()        
print(",".join(map(str,list2)))        



