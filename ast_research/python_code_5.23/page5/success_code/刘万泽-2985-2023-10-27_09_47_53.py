student = eval(input())
info = tuple(student)[1:3]
avg = sum(list(student)[-1])/len(list(student)[-1])
print(info)
print("%.2f"%avg)

