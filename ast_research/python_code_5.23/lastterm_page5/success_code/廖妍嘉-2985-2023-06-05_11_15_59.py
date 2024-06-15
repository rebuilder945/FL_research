student = eval(input())
info = (tuple(student)[1],tuple(student)[2])
avg = sum(student[-1])/len(student[-1])
print(info)
print("%.2f"%avg)

