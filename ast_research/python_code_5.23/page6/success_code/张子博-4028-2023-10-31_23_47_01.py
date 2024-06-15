def sushu(x):
    for i in range(2,x):
            if i==0 or i==1:
                return False
            if x%i==0:
                return False
    return True
def huiwen(x):
    if str(x)==str(x)[::-1]:
        return True
    else:
        return False
            
    
x=eval(input())
if x<2 or type(x)!=type(1):
    print("illegal input")
else:
    for i in range(2,x):
        if huiwen(i) and sushu(i):
           print(i,end=" ")

            



