student = eval(input())
info = tuple(student)[1:3]
avg = (tuple(student)[-1][0]+tuple(student)[-1][1]+tuple(student)[-1][2])/len(tuple(student)[-1])
print(info)
print("%.2f"%avg)

