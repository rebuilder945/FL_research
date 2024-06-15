s = eval(input())
t = True
if 100 < s < 243:
    for i in range(100,s):
        a = i%10
        b = i//10%10
        c = i//100%10
        if i == c*c + b*b + a*a:
            print(i)
            t = False
elif s >= 243:
    for i in range(100,243):
        a = i%10
        b = i//10%10
        c = i//100%10
        if i == c*c + b*b + a*a:
            print(i)
            t = False
if t:
    print("none")

