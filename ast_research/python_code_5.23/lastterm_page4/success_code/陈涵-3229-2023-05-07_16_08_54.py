num=eval(input())
num3=[]
for x in num:
    cnt=num.count(x)
    if cnt==1:
        num3.append(x)
if num3==[]:
    print("False")
else:
    num3.sort()
    for x in num3:
        print(x,end=',')  
     


        
            

           




    

