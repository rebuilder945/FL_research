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
    if ((ls[-1]==1 and n==0)or(ls[-1]==0 and n==1)or(ls[-1]=="X" and n==2)or(ls[-1]==9 and n==3)or(ls[-1]==8 and n==4)or(ls[-1]==7 and n==5)or(ls[-1]==6 and n==6)or(ls[-1]==5 and n==7)or(ls[-1]==4 and n==8)or(ls[-1]==3 and n==2)or(ls[-1]==2 and n==10)):        
        print("Correct")
    else:
        print("Wrong")
   
    

