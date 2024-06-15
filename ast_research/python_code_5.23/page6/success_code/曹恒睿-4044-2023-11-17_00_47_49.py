n = eval(input())
shuixianshu = []
for x in range(0,n+1):
    x = str(x)
    sum = 0
    for i in x:
        i = int(i)
        sum += i
    if sum == x:
        print(x)
        shuixianshu.append(x)
    else:
        pass
if shuixianshu == []:
    print("none")
    

