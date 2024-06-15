student = eval(input())
info = tuple(student[i] for i in range(1,3))
avg = sum([x for x in student[-1]])/len(student[-1])
print(info)
print("%.2f"%avg)

