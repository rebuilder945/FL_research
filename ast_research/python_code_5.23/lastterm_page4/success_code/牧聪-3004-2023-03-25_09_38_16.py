list=eval(input())
nums=[]
for n in list:
    if n >= 2:       
        for i in range(2, n):
            if n % i == 0:
                break
        nums.append(n)
    else:
        continue
print(nums)

