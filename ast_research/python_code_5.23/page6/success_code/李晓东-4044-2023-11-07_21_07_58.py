n = eval(input())
b = 0
flag = 0
if n<=100:
    print("none")
if n>=1000:
    for x in range(100,1000):
        for i in range(3):
            a = x%10
            b = b+a**3
            x = x//10
        if x ==b:
            flag = 1
            print(b)
    if flag==0:
        print("none")
else:
    for i in range(100,n):
        for i in range(3):
            a = x%10
            b = b+a**3
            x = x//10
        if x ==b:
            flag = 1
            print(b)
    if flag==0:
        print("none")




        



