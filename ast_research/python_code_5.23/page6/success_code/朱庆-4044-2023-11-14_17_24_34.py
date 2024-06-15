n = int(input())
if n>100 :
    for x in range(100,n+1):
        g = x%10
        s = x//10%10
        b = x//100
        if g**3+s**3+b**3 == x and x<1000:
            print(x)
else:
    print("none")            

