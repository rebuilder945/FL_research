def sushu(x):
    if x<=1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    else:
        return True
ls=eval(input())
ls2=[]
for n in ls:
    if sushu(n):
        ls2.append(n)
print(ls2)




        

            


        
