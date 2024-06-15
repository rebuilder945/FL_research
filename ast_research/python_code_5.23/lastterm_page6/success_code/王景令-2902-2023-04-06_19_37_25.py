def aaa(n):
    a = [1,1]
    for i in range(n):
        a.append(a[-1]+a[-2])
    b = []
    for i in range(n):
        b.append(a[i+2]/a[i+1])
    return sum(b)
a = eval(input())
print('%.4f'%aaa(a))
