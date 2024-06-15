def yanzheng(id):
    if id[-1]=="X":
        lst1=[int(x) for x in id[:17]]+[10]
    else:
        lst1=[int(x) for x in id]
    lst2=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    lst3=[]
    for i in range(len(lst1)-1):
        a=lst1[i]*lst2[i]
        lst3.append(a)
    n=sum(lst3)%11
    m=(12-n)%11
    if m==10:
        return "X"
    else:
        return m


    
id=input()
if len(id)!=18:
    print("Error")
elif len(id)==18 and id[-1]==str(yanzheng(id)):
    print("Correct")
elif len(id)==18 and id[-1]!=str(yanzheng(id)):
    print("Wrong")



