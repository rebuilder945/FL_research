student = eval(input())
info = tuple(student.numbers[1:3])
avg = sum(student.numbers[5]/len(student.numbers[5]))
print(info)
print("%.2f"%avg)

