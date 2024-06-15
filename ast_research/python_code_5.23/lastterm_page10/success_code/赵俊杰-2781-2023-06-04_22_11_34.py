str1=input()
if len(str1)==18:
    ls=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    m=0
    for x in range(len(ls)):
        m=m+int(str1[x])*ls[x]
    n=m%11
    y=(12-n)%11
    if str1[-1]=="X":
        if y==10:
            print("Correct")
    else:
        if int(str1[-1])==y:
            print("Correct")
        else:
            print("Wrong")
else:
    print("Error")
