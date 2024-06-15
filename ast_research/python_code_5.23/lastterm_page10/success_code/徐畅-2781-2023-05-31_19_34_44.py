lst=list(input())
if len(lst)!=18:
    print("Error")
else:
        a=0
        lst1=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
        for i in range(len(lst)-1):
            if lst[i]!="X":
                s=eval(lst[i])*lst1[i]
                a=a+s
        b=a%11
        lst3=["1","0","X","9","8","7","6","5","4","3","2"]
        if lst3[b]==lst[-1]:
                print("Correct")
        else:
                print("Wrong")



        
