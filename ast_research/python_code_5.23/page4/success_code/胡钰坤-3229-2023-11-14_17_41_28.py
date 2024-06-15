# nums = eval(input())
# ls = []
# for i in nums:
#     if nums.count(i) == 1:
#         ls.append(i)
# if len(ls) > 0:
#     ls.sort()
#     ls = ','.join(str(i) for i in ls)
#     print(ls)
# else:
#     print("False")

nums = eval(input())
ls = []
flag = False
for i in nums:
    if nums.count(i) == 1:
        ls.append(i)
    ls.sort()
    flag = True
else:
    flag = False
if flag == True:
    ls = ','.join(str(i) for i in ls)
    print(ls)
else:
    print("False")
