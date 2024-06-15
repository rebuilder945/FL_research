student = eval(input())
info = tuple(student)[0:2]
avg = sum(tuple(student)[-1])/3
print(info)
print("%.2f"%avg)

