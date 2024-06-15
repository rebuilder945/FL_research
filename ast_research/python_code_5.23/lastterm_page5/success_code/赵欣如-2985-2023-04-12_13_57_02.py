student = eval(input())
info = set(student[1:3])
avg = sum(set(student[-1]))/len(set(student[-1]))
print(info)
print("%.2f"%avg)

