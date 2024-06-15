student = eval(input())
info = (student[1], student[2])
 scores = student[5]
avg = sum(scores) / len(scores)
print(info)
print("%.2f"%avg)

