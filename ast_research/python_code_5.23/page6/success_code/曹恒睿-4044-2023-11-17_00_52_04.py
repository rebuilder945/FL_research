n = eval(input())
shuixianshu = []
for x in range(0,n+1):
    x = str(x)
    sum = 0
    for i in x:
        i = (int(i))**3
        sum += i
    if sum == int(x):
        print(x)
        shuixianshu.append(int(x))
    else:
        pass
if shuixianshu == []:
    print("none")
    

