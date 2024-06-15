lst=eval(input())
jack=[]
lis=[]
lis.append(max(lst))
lis.append(min(lst))
for i in lst:
    if i not in lis:
        jack.append(i)
print(jack)
    
