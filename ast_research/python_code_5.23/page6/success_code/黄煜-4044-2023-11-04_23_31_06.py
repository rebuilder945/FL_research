a=eval(input())
for i in range(0,a):
    b=a%10
    c=int(a%100/10)
    d=int(a/100)
    if b**3+c**+d**3==a:
        print(a)
    else:
        print("none")
        break
