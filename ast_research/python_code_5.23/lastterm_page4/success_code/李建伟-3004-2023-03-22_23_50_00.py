def sushu(nums):
    for i in range(2,nums):
        if nums%i == 0:
            return False
lst1 = []
lst = eval(input())
if 1 in lst:
    lst.remove(1)
elif 0 in lst:
    lst.remove(0)
else:
    for x in lst:
        if sushu(x) != False:
            lst1.append(x)
        print(lst1)
