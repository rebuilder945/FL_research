student = eval(input())
info = tuple(student[1:3])
avg = sum(tuple(student[-1]))/len(student)
print(info)
print("%.2f"%avg)

