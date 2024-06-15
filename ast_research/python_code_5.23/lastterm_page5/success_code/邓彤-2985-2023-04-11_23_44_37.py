student = eval(input())
info = tuple(x for x in [student][1][2])
avg = sum(x for x in [student][5])/len([student][5])
print(info)
print("%.2f"%avg)

