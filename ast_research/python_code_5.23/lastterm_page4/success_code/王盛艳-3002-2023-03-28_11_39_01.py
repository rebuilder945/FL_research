numbers = list(eval(input()))
avg = sum(numbers)/len(numbers)
if type(avg) == int:
    print("%d"%avg)
elif type(avg) == float:
    print("%.2f"%avg)
