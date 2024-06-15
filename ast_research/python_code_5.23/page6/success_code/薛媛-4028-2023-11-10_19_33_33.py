n=eval(input())
if type(n)==int:
    for i in range(1,n):
        m=str(i)[-1::-1]
        if str(i)==m:
            print(i,end=" ")
else:
    print("illegal input")
        
