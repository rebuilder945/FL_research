a=list(input())
if len(a)!=18:
    print("Error")
else:
    b=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    c=["1","0","X",'9','8','7','6','5','4','3',"2"]
    d=0
    for i in range(len(b)):
        sum+=int(a[i])*b[i]
    e=sum%11
    if d[e]==a[-1]:
        print("Correct")
    else:
        print("Wrong")

