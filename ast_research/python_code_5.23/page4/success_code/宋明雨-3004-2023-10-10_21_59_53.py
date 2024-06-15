def prime(nums):
    if nums == 1:
        List1.append(nums)
    elif nums == 2:
        pass    
    else:
        for i in range(2,nums-1):
            if nums % i == 0:
                List1.append(nums)
                break
List = eval(input())
List1 = []
for n in List:
    D = prime(n)
List2 = []
for x in List:
    if x not in List1 and x not in List2:
        List2.append(x)
print(List2)
