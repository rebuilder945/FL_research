num1 = eval(input())
List1 = list(range(37))
if num1 in range(0, 37):
    for x in range(len(List1)):
        if x == 0:
            List1[x] = "green"
        elif x in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 29, 30, 32, 34, 36]:
            List1[x] = "red"
        else:
            List1[x] = "black"
    print(List1[num1])
else:
    print("error")


