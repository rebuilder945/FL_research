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
    num4=[str(x) for x in num3]
    print(",".join(num4)) 
     


        
            

           




    

