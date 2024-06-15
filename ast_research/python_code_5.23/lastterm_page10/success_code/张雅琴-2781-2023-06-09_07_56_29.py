a=input()
if len(a)!=18:
    print("Error")
else:
    lst1=[]
    lst2=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]    
    lst3=["1","0","X","9","8","7","6","5","4","3","2"]
    lst4=[]
    for i in range(0,18):
        lst1.append(a[i])
    for i in range(0,17):
        lst4.append(int(a[i])*lst2[i])
    b=sum(lst4)%11
    if a[-1]==lst3[b]:
        print("Correct")
    else:
        print("Wrong")

