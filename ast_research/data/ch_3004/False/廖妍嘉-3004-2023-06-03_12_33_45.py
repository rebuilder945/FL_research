def sushu(x):
    if x<2:
        return False
    if x==2:
        return True
    if x>2:
        for i in range(2,x):
            if x%i==0:
                return  False
ls=eval(input())
ls2=[]
for n in ls:
    if sushu(n):
        ls2.append(n)
print(ls2)

            


        
