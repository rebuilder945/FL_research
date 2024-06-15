lst=eval(input())
lst1=lst.copy()
for i in lst1:
    a=lst.count(i)
    if a >=2:
       lst.remove(i)
print(lst) 
    
