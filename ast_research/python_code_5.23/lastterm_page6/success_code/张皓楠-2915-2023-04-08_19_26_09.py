s = eval(input())
t = True
if 100 <= s < 1000:
    for i in range(100,s):
        a = i%10
        b = i//10%10
        c = i//100%10
        if i == c**3 + b**3 + a**3:
            print(i)
            t = False
elif s >= 1000:
    for i in range(100,1000):
        a = i%10
        b = i//10%10
        c = i//100%10
        if i == c**3 + b**3 + a**3:
            print(i)
            t = False
if t:
    print("none")

