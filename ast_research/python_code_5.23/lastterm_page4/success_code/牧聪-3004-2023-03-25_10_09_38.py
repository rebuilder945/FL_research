lst = eval(input())
nums = []
for n in lst: 
    if n>=2 : 
        if all(n % i != 0 for i in range(2,n)):
            nums.append(n)
    else:
        continue
print(nums)

