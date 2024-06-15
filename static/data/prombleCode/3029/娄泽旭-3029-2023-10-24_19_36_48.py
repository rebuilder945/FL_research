a = input().split(",")
# print(a)
b = eval(input())
c = len(a)
# c = []
# for i in range(len(a)):
#     c.append([a[i],b[i]])
d = [[a[i],b[i]] for i in range(c)]
print(d)



