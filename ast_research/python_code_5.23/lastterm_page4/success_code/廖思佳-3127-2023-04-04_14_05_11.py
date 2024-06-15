n=eval(input())
list1=[x for x in range(1,n+1)]
list2=[]
for a in range(len(list1)):
    if a < len(list1)-1:
        list2=list2+[list1[a+1]]

list2=list2+[list1[0]]    
print(list2)
