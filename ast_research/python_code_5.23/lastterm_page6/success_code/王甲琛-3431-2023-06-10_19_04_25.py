number = eval(input())
if number == 0:
    print("green")
elif 0 < number <= 10 or 18 < number <= 28:
    if number % 2 == 0:
        print("black")
    else:
        print("red")
elif 10 < number <= 18 or 28 < number <= 36:
    if number % 2 == 0:
        print("red")
    else:
        print("black")
else:
    print("error")


# “/”，这是传统的除法，3/2=1.5
# “//”，在python中，这个叫“地板除”，3//2=1，也就是向下取整
# “%”，这个是取模操作，也就是取余数，4%2=0，5%2=1
