def sushu(n):
    if n>=2:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
    else :
        return False
ls=eval(input())
ls1=[]
for n in ls:
    if sushu(n):
        ls1.append(n)
print(ls1)
          

