lst=eval(input())
lst1=lst.copy()
for i in lst:
    if i==0:
        lst1.remove(i)
        lst1.append(i)

print(lst1)

    



    
            


