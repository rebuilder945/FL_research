n=eval(input())
list1=[]
for x in range(1,n+1):
    list1.append(x)
list2=list1.copy()
s=list1[0]
list2.pop(0)
list2.append(s)    
print(list2)

