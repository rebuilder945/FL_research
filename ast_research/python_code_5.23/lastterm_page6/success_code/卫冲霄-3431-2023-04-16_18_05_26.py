a=eval(input())
if a==0:
    print("green")
elif 1<= a <=10:
    for i in range(1,6):
        m=2*i-1
        n=2*i
        if a==m:
            print("red")
        elif a==n:
            print("black")
elif 11<= a <= 18:
    for i in range(6,10):
        m = 2 * i - 1
        n = 2 * i
        if a == m:
            print("black")
        elif a == n:
            print("red")
elif 19<= a <=28:
    for i in range(10,15):
        m=2*i-1
        n=2*i
        if a == m:
            print("red")
        elif a==n:
            print("black")
elif 29<= a <= 36:
    for i in range(15,19):
        m=2*i-1
        n=2*i
        if a==m:
            print("black")
        elif a==n:
            print("red")
else:
    print("error")

