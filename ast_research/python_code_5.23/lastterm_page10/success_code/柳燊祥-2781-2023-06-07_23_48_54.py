s=eval(input())
lst=list(s)
if len(lst)!=18:
    print("Error")
else:
    pass
    ssum=0
    num=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    for x in range(17):
        ssum+=lst[x]*num[x]
        n=ssum%11
        m=[1,0,X,9,8,7,6,5,4,3,2]
        if (12-n)%11==m[x]:
            print("Correct")
        else:
            print("Wrong")

