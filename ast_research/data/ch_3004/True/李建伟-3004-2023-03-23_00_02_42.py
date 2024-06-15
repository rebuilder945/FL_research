def sushu(nums):
    for i in range(2,nums):
        if nums%i == 0:
            return False
lst1 = []
lst = eval(input())
for x in lst:
    if sushu(x) != False:
        lst1.append(x)
        if 1 in lst1:
            lst1.remove(1)
            if 0 in lst1:
                lst1.remove(0)
print(lst1)
