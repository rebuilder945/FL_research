ls1=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
ls2=list(x for x in input())
ls=['1','0','X','9','8','7','6','5','4','3','2']
if len(ls2)!=18:
    print("Error")
else:
    sum=0
    for i in range(len(ls1)):
        sum+=ls1[i]*int(ls2[i])
    c=sum%11
    if ls[c]==ls2[-1]:
        print("Correct")
    else:
        print("Wrong")

