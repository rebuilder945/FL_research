student = eval(input())

info = tuple(student[1:3])
#tuple[1:3]应为tuple(student[1:3])

avg = student[-1]

print(info)
print("%.2f" % avg)