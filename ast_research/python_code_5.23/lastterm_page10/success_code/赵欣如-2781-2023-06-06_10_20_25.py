ls=list(input())
print(ls)
a=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
if len(ls)!=18:
    print('Error')
else:
    n=0
    b=0
    for x in ls[0:17]:
        m=int(x)*a[b]
        b+=1        
        n=n+m
    n=n%11
    dic={0:1,1:0,2:"X",3:9,4:8,5:7,6:6,7:5,8:4,9:3,10:2}
    if dic[n]==ls[-1]:
        print("Correct")
    if dic[n]!=ls[-1]:
        print("Wrong")
   
    

