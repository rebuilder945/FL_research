nums = input().split()
num = []
n = []
n1 = int(nums[0])
n2 = int(nums[1])
if n1 >= n2 or n2 > 9 or n1 < 0:
    print('illegal input')
else:
    n = list(range(n1,n2))
    for x in range(n1*111,n2*111):
        x = str(x)
        flag = True
        for y in x:
            if x.count(y) > 1 or int(y) not in n or int(x) <100:
                flag = False
                break
        if flag == True:
            num.append(int(x))
    if len(num) == 0:
        print('illegal input')
    else:
        for z in num:
            print(z,end=' ')
