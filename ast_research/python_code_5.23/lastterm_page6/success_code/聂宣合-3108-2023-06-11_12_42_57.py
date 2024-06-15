key=list(input())
ls1=key[0:-1]
sum=0
ls2=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
ls3=["1","0","X","9","8","7","6","5","4","3","2"]
if len(key)<18:
    print("Error")
else:
    for i in range(len(ls1)):
        sum+=int(ls1[i])*int(ls2[i])
    n=sum%11
    if ls3[n]==key[-1]:
        print("Correct")
    else:
        print("Wrong")




