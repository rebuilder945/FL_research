n=input()
lst=["1","0","X","9","8","7","6","5","4","3","2"]
ls=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
if len(n)!=18:
    print("Error")
else:
    s=0
    for i in range(len(n)-1):
        s=s+ls[i]*int(n[i])
    m=s%11    

    if n[len(n)-1]==lst[m]:
        print("Correct")
    else:
        print("Wrong")    

