# 12
# n = eval(input())
# m = []
# x = False
# for a in n:
#     if n.count(a) == 1:
#         m.append(a)
#         x = True
# m.sort()
# result = ",".join(str(num) for num in m)
# if x:
#     print(result)
# else:
#     print("False")



# 13
# n = eval(input())
# for i in range(len(n)):
#     if n[i]==0:
#         n.pop(i)
#         n.append(0)
# print(n)



# 14
n = eval('['+input()+']')
a,b = input().split(',')
a = int(a)
b = int(b)
if a < len(n):
    c = n[a]
    for i in range(b):
        n.append(c)
    print(n)
else:
    print('error')
