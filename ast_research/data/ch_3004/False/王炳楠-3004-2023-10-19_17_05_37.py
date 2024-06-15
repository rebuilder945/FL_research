def sushu(a):
    if a==1 or a==2:
        return "yes"
    else:
        for i in range(2,a):
            if a%i==0:
                return "no"
                break
    return "yes"
ls=eval(input())
l=[]
for n in ls[::1]:
    if sushu(n)=="yes":
        l.append(n)
print(l)
        


    
            
