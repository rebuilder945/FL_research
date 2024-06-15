lst=eval(input())
lst1=[]
for i in range(len(lst)):
    a=lst[i]
    
    if lst.count(a)==1:
        lst1.append(a)
        
if lst1==[]:
    print('False')
else:
    lst1.sort()
    n=str(lst1)
    n=n[1:-1].strip()
    print(n)
