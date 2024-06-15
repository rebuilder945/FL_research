def sushu(n):
    if n<=1:
        return False
    elif n==2:
        return True
    elif n>2:
        for i in range(2,pow(n,0.5)):
            c=0
            if n%i==0:
                return False
            else:
                c+=1
                if c==int(pow(x,0.5)-1):
                    return True
list1=eval(input())
lst=[]
for i in list1:
    if sushu(i)==True:
        lst.append(i)
print(lst)

    
    
