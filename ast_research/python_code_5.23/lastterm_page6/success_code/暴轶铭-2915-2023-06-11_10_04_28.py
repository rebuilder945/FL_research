def flower(i):
    a = i
    a = list(str(a))
    if len(a) <= 3:
        if int(a[0])**3 + int(a[1])**3 + int(a[2])**3 == int(a[0] + a[1] + a[2]):
            c.append(i)
            print(i)
        else:
            pass
    else:
        pass

num = int(input())
c = []
for i in range(100,num+1):
    flower(i)
if len(c) == 0:
    print("none")
# num = 370
# c = []
# a = num
# a = list(str(a))
# if int(a[0])**3 + int(a[1])**3 + int(a[2])**3 == int(a[0] + a[1] + a[2]):
#     c.append(num)
#     print(num)
#     print(len(c))
