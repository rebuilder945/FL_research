

n = eval(input())
for i in range(n+1):
    g = i%10
    s = i//10%10
    b = i//100
    if g**3+ s**3+b**3 ==i:
        print(i)
