n=eval(input())
if n==0:
    print("green")
if (n>=1 and n<=10) or (n>=19 and n<=28):
    if n//2==0:
        print("black")
    else:
        print("red")
else:
    if n//2==0:
        print("red")
    else:
        print("black")
