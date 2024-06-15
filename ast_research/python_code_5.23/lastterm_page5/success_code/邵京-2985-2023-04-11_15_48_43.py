student = eval(input())
info = tuple(list(student)[i] for i in range(1,3))
avg = sum(list(student)[5])/len(list(student)[5])
print(info)
print("%.2f"%avg)

