def sushu(a):
    for i in range(2,a//2+1):
        if a%i==0:
            return False
        else:
            return True
def huiwenshu(a):
    if str(a)==str(a)[::-1]:
        return True
    else:
        return False
n=input()
if n>1 and n//1==n :
    for i in range(2,n):
        if sushu(n) and huiwenshu(n):
            print(i,end=" ")

    
else:
    print("illegal input")


     




                

