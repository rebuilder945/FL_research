num=eval(input())
num2=[]
num3=[]
for x in num:
    cnt=num.count(x)
    num2.append(cnt)
    if cnt==1:
        num3.append(x)
num3.sort()
num4=[str(x) for x in num3 ]
if min(num2)>1:
    print(min(num2)==1)
else:
    print(",".join(num4))    
     


        
            

           




    

