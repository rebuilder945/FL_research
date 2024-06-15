student = eval(input())
info = (student[1], student[2])
avg = round(sum(scores)/len(scores), 2)
print(info)
print("%.2f"%avg)

