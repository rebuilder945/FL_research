op = list(input())
if len(op) != 18:
    print("Error")
else:
    tem = map(lambda x, y: x * int(y), [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2], op)
    n = sum(tem) % 11
    m = 0
    if op[17] == 'X':
        m = 10
    else:
        m = int(op[17])
    if m == (12 - n) % 11:
        print("Correct")
    else:
        print("Wrong")

