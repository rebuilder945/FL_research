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
n=eval(input())
if n<2 or type(n)!=type(1):
    print("illegal input")
else:
    for i in range(2,n):
        if sushu(n) and huiwenshu(n):
            print(i,end=" ")
   


     




                

