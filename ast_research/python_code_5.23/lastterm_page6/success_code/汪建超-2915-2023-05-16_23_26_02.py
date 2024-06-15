# def isS(x):
#     a = x//100
#     b = x//10
#     c = x %10
#     if a**3+b**3+c**3 ==x:
#         return True
# n = int(input())
# lst = []
# for i in range (0,n):
#     if isS(i):
#         lst.append(i)
# if lst==[]:
#     print("none")
# else:
#     print(*lst)
n = int(input(""))

is_find = False # 标记是否找到了水仙花数

# 遍历所有三位数
for i in range(100, n + 1):
    a = i // 100 # 百位数
    b = i // 10 % 10 # 十位数
    c = i % 10 # 个位数
    
    if i == a**3 + b**3 + c**3:
        print(i)
        is_find = True

# 如果没有找到任何水仙花数，输出"none"
if not is_find:
    print("none")

