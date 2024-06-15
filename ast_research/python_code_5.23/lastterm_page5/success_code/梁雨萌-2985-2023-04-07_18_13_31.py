student = eval(input())
info = tuple(student[1:3:1])
avg = sum(student[-1])/len(student[-1])
print(info)
print("%.2f"%avg)

