student = eval(input())
info = student[1:2]
avg = sum(student[-1:-2])/len(student[-1:-2])
print(info)
print("%.2f"%avg)

