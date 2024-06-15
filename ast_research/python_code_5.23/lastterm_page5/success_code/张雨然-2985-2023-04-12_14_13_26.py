student = eval(input())
info = tuple(student(2),student(3))
avg = sum(list(student[-1]))/len(list(student[-1]))
print(info)
print("%.2f"%avg)

