student = eval(input())
info = tuple(student[1:3:1])
avg = sum(info)/len(info)
print(info)
print("%.2f"%avg)

