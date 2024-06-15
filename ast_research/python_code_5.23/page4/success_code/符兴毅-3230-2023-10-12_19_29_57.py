aim = eval(input())
reach = str(max(aim))
aim.remove(max(aim))
for i in range(len(aim)):
    max1 = max(aim)
    reach = reach + str(max1)
    aim.remove(max1)
if reach==str(0)*len(reach):
    print(0)
else:
    print(reach)
