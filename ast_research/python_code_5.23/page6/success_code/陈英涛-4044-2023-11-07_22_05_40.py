n = eval(input())
flag = False
if 1000>n>100:
    for i in range(100,n+1):
        a = i%10
        b = i//10%10
        c = i//100
        if a**3 + b**3 + c**3 == i:
            print(i)
            flag = True
if flag==False:
    print("none") 

            
    

