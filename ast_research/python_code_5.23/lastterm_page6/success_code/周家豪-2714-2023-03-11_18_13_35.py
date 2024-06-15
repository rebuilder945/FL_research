def evaluation(mark):    
    if 90 <= mark <= 100:
        print("A")
    elif mark >= 80:
        print("B")
    elif mark >= 70:
        print("C")
    elif mark >= 60:
        print("D")
    elif 0 <= mark < 60:
        print("E")
    else:
        print("error")

k=eval(input())
evaluation(k)
