a=eval(input())
for i in range(0,a):
    b=i%10
    c=int(i%100/10)
    d=int(i/100)
    if b**3+c**+d**3==a:
        print(a)
    else:
        print("none")
        break
