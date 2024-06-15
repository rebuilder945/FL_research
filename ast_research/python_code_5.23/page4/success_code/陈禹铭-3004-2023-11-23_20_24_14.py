x=int(input())
def sushu(x):

    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
        
    return True
for y in range(2,(x+1)//2):
    z=x-y
    if sushu(z) and sushu(y):
        print("%d=%d=%d"%(x,y,z))
        break



        
