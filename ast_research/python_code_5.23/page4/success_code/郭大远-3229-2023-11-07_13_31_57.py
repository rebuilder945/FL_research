list1=eval(input())
list2=[]
for x1 in list1:
    n=list1.count(x1)
    if n==1:
        list2.append(x1)
        print(','.jion(str(x) for x in list2))
    
    
