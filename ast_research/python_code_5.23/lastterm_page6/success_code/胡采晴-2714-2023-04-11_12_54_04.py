def test_mark():
    mark = input()
    try:
        mark = float(mark)
    except:
        print("data error!")
        return
    if 90 <= mark <= 100:
        print("A")
    elif 80 <= mark < 90:
        print("B")
    elif 70 <= mark < 80:
        print("C")
    elif 60 <= mark < 70:
        print("D")
    elif 0 <= mark < 60:
        print("E")
    else:
        print("data error!")


test_mark()
