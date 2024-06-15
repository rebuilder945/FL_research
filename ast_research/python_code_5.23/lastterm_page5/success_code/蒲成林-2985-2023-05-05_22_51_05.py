student = eval(input())
info = (student[1], student[2])
avg = round(sum(student[5])/len(student[5]), 2)
print(info)
print("%.2f"%avg)

