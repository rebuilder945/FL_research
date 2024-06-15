lst=eval(input())
lst.sort()
bst=lst[:]

for x in lst:
    if lst.count(x)>1:
        lst.remove(x)
for x in lst:
    if lst.count(x)>1:
        lst.remove(x)
n=len(lst)
sum=0
for i in lst:
    if bst.count(i)==1:
        sum+=i*10**(bst.index(i))
    else:
        sum+=i*10**(bst.index(i))+i*10**(bst.index(i)+1)
    
    

print(sum)
