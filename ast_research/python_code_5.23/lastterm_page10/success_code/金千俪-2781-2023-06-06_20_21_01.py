a=input()
if len(a)!=18:
    print("Error")
else:
    lst1=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    lst2=list(a[:17])
    lst3=[lst1[x]*lst2[x] for x in range(len(lst1))]
    s=sum(lst3)
    y=s%11
    m=(12-y) % 11
    if str(m)==a[-1] or (m==10 and a[-1]=='X'):
        print("Correct")
    else:
        print("Wrong")
