n = eval(input())
for i in range(n+1):
    if 99<i<1000:
        a = i % 10
        b = int(a//10)
        c = b%10
        d = int(b//10)
        if a**3 + c**3+d**3==i:
            print(i)
        else:
            print("none")
