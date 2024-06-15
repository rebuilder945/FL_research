a=eval(input())
for x in range(100,a+1):
    b=int(str(x)[0])
    c=int(str(x)[1])
    d=int(str(x)[2])
    if b**3+c**3+d**3==a:
        print(x)
else:
    print("none")    
