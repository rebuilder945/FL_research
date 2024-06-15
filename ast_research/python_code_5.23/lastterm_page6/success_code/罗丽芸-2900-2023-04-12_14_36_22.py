a=eval(input())
if a<0:
    print("illegal input")
elif type(a)!=type(1):
    print("illegal input")
else: 
    for i in range(a):
        if i in [2,3,5,7,11,101,131,151,181,191,313,353,373,383,727,757,787,797,919,929]:
            print(i,end=" ")
        else:
            pass 



