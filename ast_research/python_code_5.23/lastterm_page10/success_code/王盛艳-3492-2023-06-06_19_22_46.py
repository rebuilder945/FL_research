s = input()
list1 = list(s)
cishu1 = 0
for x in list1:
    cishu = 0
    for x2 in list1:
        if x == x2:
            cishu += 1
    if cishu == 1:
        print(x)
        cishu1 += 1
        break
if cishu1 == 0:
    print("None")
