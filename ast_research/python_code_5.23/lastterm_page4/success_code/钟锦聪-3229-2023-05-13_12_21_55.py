# def orange(num):
#     for x in num:
#         a = num.count(x)
#         if a == 1:
#             return True   
#     return False
# num = eval(input())
# sub = []
# if orange(num):
#     for x in num:
#         a = num.count(x)
#         if a == 1:
#             sub.append(x)
#     sub.sort()
#     print(*sub,sep=",")
# else:
#     print("False")
num = eval(input())
nums = []
for x in num:
    if x not in nums:
        nums.append(x)
numss = []
for i in nums:
    a = num.count(i)
    if a ==1:
        numss.append(i)
numss.sort()
if len(numss)>=1:
    print(*numss,sep =',')
else:
    print("False")
