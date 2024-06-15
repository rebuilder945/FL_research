num=list(input())
if len(num)!=18:
    print('Error')
else:
    n=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    lastn=['1','0','X','9','8','7','6','5','4','3','2']
    for i in range(len(n)):
        sum+=int(id[i]*n[i])
    lasti=sum%11
    if lastn[lasti]==id[-1]:
        print("Correct")
    else:
        print("Wrong")

