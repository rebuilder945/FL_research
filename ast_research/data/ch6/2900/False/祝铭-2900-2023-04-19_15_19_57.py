n = eval(input())

if n % 1 != 0 or n < 0:
    print("illegal input")
else:
    for x in range(n):
        if x>=2:
            for y in range(2,x,1):
                if x%y==0:
                    break
            else:
                if str(x) == str(x)[::-1]:
                    print(x,end=" ")

