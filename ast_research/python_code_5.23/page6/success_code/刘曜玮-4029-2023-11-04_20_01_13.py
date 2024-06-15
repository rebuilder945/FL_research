x = (input().split(" "))
n = eval(x[0])
m = eval(x[1])
if n > m or m-n != 3 or n >= 8:
    print("illegal input")
else:
    a = str(n)
    b = str(n+1)
    c = str(n+2)
    print(a+b+c,a+c+b,b+a+c,b+c+a,c+a+b,c+b+a)




    


