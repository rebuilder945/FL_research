student = eval(input())
info = (student[1], student[2])
avg = sum(student[3:]) / len(student[3:])
print(info)
print("%.2f"%avg)

