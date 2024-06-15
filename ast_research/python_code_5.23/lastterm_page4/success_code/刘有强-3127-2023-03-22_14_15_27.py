a=int(input())
lst=[x for x in range(1,a+1)]
lst2=[]
for i in lst[1:]:
       lst2.append(i)
lst2.append(1) 
print(lst2)
