list1=eval(input())
list2=[]
for x in list1:
    if list1.count(x)==1:
        list2.append(x)
    else :
         print("False")
         break       
list2.sort()        
print(",".join(map(str,list2)))        



