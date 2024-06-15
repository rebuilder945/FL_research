def su(x):
    flag = True
    if x in [1,2,3]:
        flag = False
    else:
        for y in range(2,x+2//2):
            if x % y ==0:
                flag = False
                break
    if flag == True:
        return True
    else:
        return False

num = eval(input())
nums = []
for z in num:
    if su(z):
        nums.append(z)
print(nums)
