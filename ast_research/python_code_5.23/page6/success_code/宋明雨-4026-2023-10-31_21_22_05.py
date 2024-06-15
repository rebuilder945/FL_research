def shu_lie(n):
    b,a = 2,1
    A = b/a
    sum = 0
    for i in range(n):
        c = b + a
        a = b
        b = c
        sum = sum + A
        A = c / a 
    print("%.4f"%sum)
n = eval(input())
shu_lie(n)


