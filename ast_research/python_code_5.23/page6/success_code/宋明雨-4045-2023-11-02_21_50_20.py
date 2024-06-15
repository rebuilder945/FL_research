def achievement(A):
    if A < 60:
        print("E")
    elif A < 70:
        print("D")
    elif A < 80:
        print("C")
    elif A < 90:
        print("B")
    else:
        print("A")
A = eval(input())
achievement(A)

