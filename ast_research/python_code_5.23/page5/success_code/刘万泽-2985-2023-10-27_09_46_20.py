student = eval(input())
info = tuple(student)[2:4]
avg = sum(list(student)[-1:-2])/3
print(info)
print("%.2f"%avg)

