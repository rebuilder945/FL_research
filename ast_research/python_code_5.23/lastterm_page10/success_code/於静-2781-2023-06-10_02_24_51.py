shuju=input()
if len(shuju)!=18:
    print("Error")
else:
    shu=shuju[17]
    xishu=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    ma=['1','0','X','9','8','7','6','5','4','3','2']
    chushi=0
    for i in range(len(xishu)):
        chushi=chushi+int(shuju[i])*xishu[i]
    shu=chushi%11
    if shu!=ma[shu]:
        print("Wrong")
    else:
        print("Correct")
