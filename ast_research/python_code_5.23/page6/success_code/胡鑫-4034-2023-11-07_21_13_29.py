n = eval(input())
m = eval(input())
if n == 'red':
    if m == 'blue':
        print("purple")
    elif m == 'yellow':
        print("orange")
elif n == 'blue':
    if m == 'yellow':
        print("green")
    if m == 'red':
        print("purple")
elif n == 'yellow':
    if m == 'blue':
        print("green")
    if m == 'red':
        print("orange")
else:
    print("error")


