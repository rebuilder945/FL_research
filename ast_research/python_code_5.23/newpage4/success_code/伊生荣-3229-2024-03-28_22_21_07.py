nums = list(input())
list1 = []
for i in nums:
    s = nums.count(i)
    if s == 1:
        list1.append(i)
        list1.sort()
        print(''.join(list1))
    else:
        print("False")
