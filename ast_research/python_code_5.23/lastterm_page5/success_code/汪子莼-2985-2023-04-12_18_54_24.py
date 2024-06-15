student = eval(input())
info = tuple(student[1:3])
avg = tuple(sum(eval(student[-1]))/3)
print(info)
print("%.2f"%avg)

