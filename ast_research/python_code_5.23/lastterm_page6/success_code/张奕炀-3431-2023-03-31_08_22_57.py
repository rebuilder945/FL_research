number = eval(input())
if number == 0:
    print("green")
elif 0 < number <= 10 or 18 < number <= 28:
    if number // 2 == 0:
        print("black")
    elif number // 2 == 1:
        print("red")
elif 10 < number <= 18 or 28 < number <= 36:
    if number // 2 == 0:
        print("red")
    elif number // 2 == 1:
        print("black")
else:
    print("error")
