ls=list(input())
a=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
if len(ls)!=18:
    print('Error')
else:
    n=0
    b=0
    for x in ls[:17]:
        m=int(x)*a[b]
        b+=1        
        n=n+m
    n=n%11
    if ls[-1]!=(12-n)%11:
        if ls[-1]=="X" and n==2:
            print("Correct")
        else:
            print("Wrong")
    if ls[-1]==(12-n)%11:
        print("Correct")
    

