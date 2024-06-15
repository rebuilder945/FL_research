lst=eval(input())
lst1=[]
for x in lst:
    if lst.count(x)==1:
        lst1.append(int(x))
        lst1.sort()
print(lst1[:])
    

    
