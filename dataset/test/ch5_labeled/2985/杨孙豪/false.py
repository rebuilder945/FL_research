student = eval(input())
info = tuple(student[1])+tuple(student[2])
avg = sum(student[5])/len(student[5])
print(info)
print("%.2f"%avg)

