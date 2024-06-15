list1=eval(input())
list2=list(list1)
k=0
sum=[]
for x in range(len(list2)):
    if list2[x]== 0 :    
        k=k+1
    if list2[x]!=0:
        sum=sum+[list2[x]]   
         
for i in range(k):
    sum=sum+[0]


print(sum)            

