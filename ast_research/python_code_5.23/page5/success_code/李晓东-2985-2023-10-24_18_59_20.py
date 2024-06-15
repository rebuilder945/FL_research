student = eval(input())
info = tuple(student)[1:3]
avg = sum(list(student))/len(list(student))
print(info)
print("%.2f"%avg)

