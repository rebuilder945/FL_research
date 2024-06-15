student = eval(input())
info = tuple(list(student)[1],list(student)[2])
avg = sum(list(student)[-1])/len(list(student))
print(info)
print("%.2f"%avg)

