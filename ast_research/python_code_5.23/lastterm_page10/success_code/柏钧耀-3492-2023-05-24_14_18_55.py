a=input()
la=len(a)
lst=[]
for i in range(la):
    lst.append(a[i])

for i in lst:
    if lst.count(i)==1:
        print(i)
        break
else:
    print('None')

    
