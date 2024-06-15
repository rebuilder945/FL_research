def huiwen(n):
    if str(x)[::-1]==str(x):
        return True
def sushu(x):
    for i in range(2,x//2+1):
        if x %i==0:
            return False

    else:
        return True
        





n=eval(input())
a=[]
if n-int(n)!=0 or n<0:
    print("illegal input")
elif n==1:
    print("illegal input")
else:   
    for x in range(2,n+1):
        if huiwen(x)and sushu(x):
            print(x,end=" ")
