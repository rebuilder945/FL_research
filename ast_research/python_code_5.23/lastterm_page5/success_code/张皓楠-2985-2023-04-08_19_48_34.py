student = eval(input())
info = tuple(list(student)[1:3])
avg = sum(eval(list(student)[5]))/len(eval(list(student)[5]))
print(info)
print("%.2f"%avg)

