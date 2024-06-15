def sushu(s):
    x = []
    for m in s:
        if m >= 2:
            for n in range (2,m,1):
                if m%n == 0:
                    break
            else:
                x.append(m)
    print(x)
nums = eval(input())
sushu(nums)
