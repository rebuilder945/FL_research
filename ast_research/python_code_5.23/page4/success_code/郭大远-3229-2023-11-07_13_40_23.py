list1=eval(input())
list2=[]
for x1 in list1:
    n=list1.count(x1)
    if n==1:
        list2.append(x1)
list2.sort()
if list2==[]:
        print("False")
else:       
        print(','.join(str(x) for x in list2))
    
    
