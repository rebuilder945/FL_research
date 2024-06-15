student = eval(input())
info = tuple(student[1:3:1])
avg = sum(tuple(student[-1]))/len(tuple(student[-1]))
print(info)
print("%.2f"%avg)

