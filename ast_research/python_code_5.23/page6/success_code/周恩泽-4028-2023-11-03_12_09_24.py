def huiwenshu(n):
    if str(n)==str(n)[::-1]:
        return True
def sushu(i):
    
    
        a=0
        for y in  range(2,i):
            if i%y==0:
                a=a+1
        if a==0:
            return True




n=eval(input())
if n<1 or type(n)!=int:
    print("illegal input")
else:
    for i  in range(2,n+1):
        if huiwenshu(i) and sushu(i):
        
             print(i)

