x = (input().split(" "))
n = eval(x[0])
m = eval(x[1])
if n > m or m-n != 3 or n >= 8 or n<0 or m<0:
    print("illegal input")
elif n==0:
    a = str(n)
    b = str(n + 1)
    c = str(n + 2)
    print(b+a+c,b+c+a,c+a+b,c+b+a)
else:
    a = str(n)
    b = str(n+1)
    c = str(n+2)
    print(a+b+c,a+c+b,b+a+c,b+c+a,c+a+b,c+b+a)




    


