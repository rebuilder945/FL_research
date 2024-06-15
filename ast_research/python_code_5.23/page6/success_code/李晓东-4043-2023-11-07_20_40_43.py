list = "".join(eval(input()))
for x in "abcdefghijklmnopqrstuvwxyz":
    if x in list:
        num = list.count(x)
        tem = x+","+str(num)
        print(tem)

