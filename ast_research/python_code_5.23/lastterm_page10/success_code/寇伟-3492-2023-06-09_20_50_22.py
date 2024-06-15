s=input()
count=0
if not s:
    ls = list(s)
    ls1=[]
    
    for i in ls:
        if ls.count(i)==1:
            ls1.append(i)
            count+=1
if count == 0:
    print('None')
else:
    print(ls1[0])

