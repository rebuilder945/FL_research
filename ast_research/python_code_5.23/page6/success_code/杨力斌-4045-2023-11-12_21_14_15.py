def rank(sorces):
    if 60 > sorces >= 0:
        print("E")
    elif 70 > sorces >= 60:
        print("D")
    elif 80 > sorces >= 70:
        print("C")
    elif 90 > sorces >= 80:
        print("B")
    elif 100 >= sorces >= 90:
        print("A")
sorted = eval(input())
rank(sorted)
