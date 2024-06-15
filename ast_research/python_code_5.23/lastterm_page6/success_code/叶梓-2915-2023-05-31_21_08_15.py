#n=eval(input())
#for i in range(2,n+1):
#    if i==n[0]**3+n[1]**2+n[2]:
#        print(n)
num1 = eval(input())
List1 = []
for x in range(2, num1 + 1):
    if 0 < x < 100:
        if (x % 10) ** 2 + (x // 10) ** 2 == x:
            List1.append(x)
        else:
            pass
    elif 100 <= x < 1000:
        if (x % 10) ** 3 + (x // 10 % 10) ** 3 + (x // 100) ** 3 == x:
            List1.append(x)
        else:
            pass
    else:
        pass
if len(List1) == 0:
    print('none')
else:
    for y in range(len(List1)):
        print(List1[y])
