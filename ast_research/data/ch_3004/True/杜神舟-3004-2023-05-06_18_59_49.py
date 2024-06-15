def sushu(n):
    if n>=2:
        for x in range(2,n):
            if n%x==0:
                return False
        else:
            return  True
    else:
        return False

lst=eval(input())
ls2=[]    
for b in lst:
    if sushu(b):
        ls2.append(b)

print(ls2)
        
                       
