def hanshu():
    x = eval(input())
    if x < 20:
        answer = 6 * pow(x,2) + 1
    elif 20 <= x < 40:
        answer = pow(3 * x - 60,0.5)
    else:
        answer = 100 / (x + 1)
    print("%.2f"%(answer))
hanshu()

