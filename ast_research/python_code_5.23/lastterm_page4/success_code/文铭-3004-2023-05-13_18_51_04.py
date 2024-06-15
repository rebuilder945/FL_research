ls = eval(input())
f = 0
l2 = []
for x in ls:
    if x>=2:
        for i in range(2,int(x**0.5)+1):
            if x % i == 0:
                f = 1
                break
            else:
                f = 0
        if f == 0:
            l2.append(x)
print(l2)
